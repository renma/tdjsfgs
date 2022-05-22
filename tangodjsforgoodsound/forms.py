# Time-stamp: <2022-05-22 09:26:26 rene>
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

import logging
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from . common import doesEmailExist, TrickyField, USEREMAIL_NOT_REGISTERED
from . models import DJ, LENGTH_1


logger = logging.getLogger("tdjsfgs")
DISABLE_AUTOCOMPLETE = True


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


class MyFormBase(forms.Form):

    any_error = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(MyFormBase, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MyFormBase, self).clean()
        for field in self.fields:
            if not field == "any_error" and not cleaned_data.get(field):
                self.add_error(field, "field cannot be empty")
                self.add_error("any_error", "field cannot be empty")
                msg = "Error because %s empty or not valid"
                logger.info(msg % field)
                if field == "contact_magic":
                    for x in self.fields:
                        val = cleaned_data.get(x)
                        if not val:
                            val = ""
                        logger.info(">>> %s = %s" % (x, val))


class ContactForm(MyFormBase):

    contact_firstname = forms.CharField(required=True)
    contact_lastname = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    attrs = {'rows': 5, 'cols': 42}
    contact_content = forms.CharField(required=True,
                                      widget=forms.Textarea(attrs=attrs))
    contact_magic = TrickyField(required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["contact_firstname"].label = "First name"
        self.fields["contact_lastname"].label = "Family name"
        self.fields["contact_email"].label = "Email address"
        self.fields["contact_content"].label = "Message (E/D)"
        self.fields["contact_magic"].label = "Magic"


class RegisterForm(MyFormBase):

    register_firstname = forms.CharField(required=True)
    register_lastname = forms.CharField(required=True)
    register_djname = forms.CharField(required=True)
    register_email = forms.EmailField(required=True)
    register_password1 = forms.CharField(widget=forms.PasswordInput(render_value=True), required=True)
    register_password2 = forms.CharField(widget=forms.PasswordInput(render_value=True), required=True)
    register_magic = TrickyField(required=True)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["register_firstname"].label = "First name"
        self.fields["register_lastname"].label = "Family name"
        self.fields["register_djname"].label = "DJ name"
        label = "Email address used for login"
        self.fields["register_email"].label = label
        self.fields["register_password1"].label = "Password"
        self.fields["register_password2"].label = "Confirm password"
        self.fields["register_magic"].label = "Magic"

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        # Email
        email = self.cleaned_data.get("register_email")
        if email:
            request = None
            if doesEmailExist(request, email):
                msg = "Email already known in the system"
                self.add_error("register_email", msg)
                self.add_error("any_error", msg)
                msg = "Error because email already known in the system"
                logger.info(msg)

        # Password
        password1 = self.cleaned_data.get("register_password1")
        password2 = self.cleaned_data.get("register_password2")
        if password1 and password2:
            ok = True
            passwords = [password1, password2]
            for password in passwords:
                try:
                    validate_password(password)
                except Exception:
                    ok = False
                    msg = "Password not valid"
                    self.add_error("register_password1", msg)
                    self.add_error("any_error", msg)
                    msg = "Error because password%d not valid"
                    logger.info(msg % (passwords.index(password) + 1))
            if ok and not password1 == password2:
                msg = "Password_mismatch"
                self.add_error("register_password2", msg)
                self.add_error("any_error", msg)
                msg = "Error because passwords mismatch"
                logger.info(msg)

        return cleaned_data


class DJEditForm(forms.ModelForm):

    attrs = {"cols": 45, "rows": 4}
    music_remark = forms.CharField(required=False,
                                   widget=forms.Textarea(attrs=attrs))
    equipment_remark = forms.CharField(required=False,
                                       widget=forms.Textarea(attrs=attrs))

    website = forms.URLField(required=False, initial='http://')
    resident_dj_website = forms.URLField(required=False, initial='http://')

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
            "resident_dj_location",
            "resident_dj_website",
            "style",
            "cortinas",
            "audioformat",
            "audioformat2",
            "songdisplay",
            "sources",
            "favorites",
            "music_remark",
            "computer",
            "computermodel",
            "musiclibrarymanagement",
            "player",
            "audiointerface",
            "equalization",
            "soundprocessor",
            "compression",
            "soundprocessor2",
            "other_equipment",
            "equipment_remark",
            "backup_computer",
            "backup_computermodel",
            "backup_player",
            "backup_audiointerface",
            # "backup_soundprocessor",
            "backup_other_equipment"]

    def __init__(self, *args, **kwargs):
        super(DJEditForm, self).__init__(*args, **kwargs)
        nonRequiredFields = [
            "email",
            "namesort",
            "website",
            "resident_dj_location",
            "resident_dj_website",
            "soundprocessor",
            "soundprocessor2",
            "audioformat2",
            "songdisplay",
            "music_remark",
            "other_equipment",
            "equipment_remark",
            "backup_audiointerface",
            # "backup_soundprocessor",
            "backup_other_equipment"]
        for field in self.fields:
            if field not in nonRequiredFields:
                self.fields[field].required = True
        self.fields["province"].widget.attrs["pattern"] = r"\D*"
        if DISABLE_AUTOCOMPLETE:
            for field in ["name",
                          "province",
                          "email",
                          "useremail",
                          "website",
                          "resident_dj_location",
                          "resident_dj_website",
                          "sources",
                          "favorites",
                          "computermodel",
                          "musiclibrarymanagement",
                          "player",
                          "audiointerface",
                          "soundprocessor",
                          "soundprocessor2",
                          "other_equipment",
                          "backup_computermodel",
                          "backup_player",
                          "backup_audiointerface",
                          # "backup_soundprocessor",
                          "backup_other_equipment"]:
                self.fields[field].widget.attrs["autocomplete"] = "off"

    def clean(self):
        cleaned_data = super(DJEditForm, self).clean()

        anyError = False

        x = cleaned_data.get("soundprocessor")
        if not cleaned_data.get("equalization") == "NEV" and \
           (not x or x.startswith("-")):
            self.add_error("soundprocessor", "Cannot be empty")
            anyError = True

        x = cleaned_data.get("soundprocessor2")
        if not cleaned_data.get("compression") == "NEV" and \
           (not x or x.startswith("-")):
            self.add_error("soundprocessor2", "Cannot be empty")
            anyError = True

        if (len(cleaned_data.get("music_remark")) > LENGTH_1 - 1):
            self.add_error("music_remark", "to long")
            anyError = True

        if (len(cleaned_data.get("equipment_remark")) > LENGTH_1 - 1):
            self.add_error("equipment_remark", "to long")
            anyError = True

        userEmail = cleaned_data.get("useremail")
        logger.info("%s, known: %s" % (userEmail, doesEmailExist(self.request, userEmail)))
        if userEmail and doesEmailExist(self.request, userEmail):
            msg = "Email already known in the system"
            self.add_error("useremail", msg)
            anyError = True

        publicEmail = cleaned_data.get("email")
        logger.info("%s, known: %s" % (publicEmail, doesEmailExist(self.request, publicEmail)))
        if publicEmail and doesEmailExist(self.request, publicEmail):
            msg = "Email already known in the system"
            self.add_error("email", msg)
            anyError = True

        for field in self.fields:
            if self.fields[field].required:
                if field not in self.cleaned_data:
                    anyError = True
                    logger.info("Error because %s not set" % field)
                else:
                    try:
                        if self.cleaned_data[field].startswith("-"):
                            anyError = True
                            msg = "Error because %s startswith '-'"
                            logger.info(msg % field)
                            msg = "Error because value invalid"
                            self.add_error(field, msg)
                    except AttributeError:
                        pass  # not a text field

        if anyError:
            self.add_error("namesort", "error")

        return cleaned_data

    def set_namesort(self, request):
        """
        Carlos Di Sarli => sarli
        Maurer => maurer
        roo daa dii DOO => doo
        """
        mutable = request.POST._mutable
        request.POST._mutable = True
        if self.data["name"]:
            x = self.data["name"].split()
            namesort = x[1] if "dj" in x[0].lower() and len(x) > 1 else x[0]
            self.data["namesort"] = namesort.lower()[:40]
        # print "used namesort =", self.data["namesort"]
        request.POST._mutable = mutable
