# Time-stamp: <2017-12-14 10:37:22 rene>
#
# Copyright (C) 2017 Rene Maurer
# This file is part of tangodjsforgoodsound.
#
# tangodjsforgoodsound is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# tangodjsforgoodsound is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------

from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from . common import TrickyField, USEREMAIL_NOT_REGISTERED
from . models import DJ, LENGTH_1


class SubscriberPasswordForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        for password in [password1, password2]:
            validate_password(password)
        if not password1 == password2:
            msg = "Password_mismatch"
            raise forms.ValidationError(msg, code=msg)


class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email,
                                   is_active=True).exists():
            raise ValidationError(USEREMAIL_NOT_REGISTERED)
        return email


class ContactForm(forms.Form):

    contact_firstname = forms.CharField(required=True)
    contact_lastname = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    attrs = {'rows': 5, 'cols': 42}
    contact_content = forms.CharField(required=False,
                                      widget=forms.Textarea(attrs=attrs))
    contact_magic = TrickyField(required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["contact_firstname"].label = "Your first name"
        self.fields["contact_lastname"].label = "Your family name"
        self.fields["contact_email"].label = "Your email address"
        self.fields["contact_content"].label = "Your message (E/D)"
        self.fields["contact_magic"].label = "One of the big four orchestras"


class DJEditForm(forms.ModelForm):

    attrs = {"cols": 45, "rows": 4}
    music_remark = forms.CharField(required=False,
                                   widget=forms.Textarea(attrs=attrs))
    equipment_remark = forms.CharField(required=False,
                                       widget=forms.Textarea(attrs=attrs))

    class Meta:
        model = DJ
        fields = [
            # "user",
            "namesort",
            "name",
            "gender",
            "country",
            "province",
            "since",
            "number_of_milongas",
            "email",
            "useremail",
            "website",
            "style",
            "cortinas",
            "audioformat",
            "audioformat2",
            "sources",
            "favorites",
            "music_remark",
            "computer",
            "computermodel",
            "player",
            "audiointerface",
            "soundprocessor",
            "other_equipment",
            "compression",
            "equalization",
            "equipment_remark",
            "backup_computer",
            "backup_computermodel",
            "backup_player",
            "backup_audiointerface",
            "backup_soundprocessor",
            "backup_other_equipment"]

    def __init__(self, *args, **kwargs):
        super(DJEditForm, self).__init__(*args, **kwargs)
        nonRequiredFields = [
            "namesort",
            "website",
            "soundprocessor",
            "audioformat2",
            "music_remark",
            "other_equipment",
            "equipment_remark",
            "backup_audiointerface",
            "backup_soundprocessor",
            "backup_other_equipment"]
        for field in self.fields:
            if field not in nonRequiredFields:
                self.fields[field].required = True
        self.fields["province"].widget.attrs["pattern"] = "\D*"

    def clean(self):
        cleaned_data = super(DJEditForm, self).clean()

        if (not cleaned_data.get("compression") == "NEV"
                or not cleaned_data.get("equalization") == "NEV") and \
                not cleaned_data.get("soundprocessor"):
            self.add_error("soundprocessor", "Cannot be empty")

        if (len(cleaned_data.get("music_remark")) >= LENGTH_1 - 1):
            self.add_error("music_remark", "to long")

        if (len(cleaned_data.get("equipment_remark")) >= LENGTH_1 - 1):
            self.add_error("equipment_remark", "to long")

        useremailError = True
        try:
            theUser = User.objects.filter(id=self.request.user.id)[0]
            if theUser:
                loginAddress = cleaned_data.get("useremail")
                if loginAddress == theUser.username \
                   and loginAddress == theUser.email:
                    useremailError = False
                else:
                    try:
                        x = theUser.id
                        y = loginAddress
                        objects = User.objects.exclude(id=x).filter(email=y)
                        if not objects:
                            useremailError = False
                    except Exception:
                        pass
        except Exception:
            pass
        if useremailError:
            # use namesort to indicate this Error (HACK!)
            self.add_error("useremail", "Not unique or user not found")
            self.add_error("namesort", "Not unique or user not found")

        return cleaned_data

    def set_namesort(self, request):
        """
        Carlos Di Sarli => sarli
        Maurer => maurer
        roo daa dii DOO => doo
        """
        mutable = request.POST._mutable
        request.POST._mutable = True
        x = self.data["name"].split()
        namesort = x[1] if "dj" in x[0].lower() and len(x) > 1 else x[0]
        self.data["namesort"] = namesort.lower()[:40]
        # print "used namesort =", self.data["namesort"]
        request.POST._mutable = mutable
