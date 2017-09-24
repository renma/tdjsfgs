from django import forms
from . common import TrickyField
from . models import DJ


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
        self.fields["contact_content"].label = "Your message"
        self.fields["contact_magic"].label = "One of the big four orchestras"


class DJEditForm(forms.ModelForm):

    class Meta:
        model = DJ
        fields = [
            # "user",
            "name",
            "gender",
            "country",
            "since",
            "number_of_milongas",
            "email",
            "website",
            "style",
            "cortinas",
            "audioformat",
            "audioformatmat2",
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
            "website",
            "soundprocessor",
            "audioformatmat2",
            "music_remark",
            "other_equipment",
            "equipment_remark",
            "backup_audiointerface",
            "backup_soundprocessor",
            "backup_other_equipment"]
        for field in self.fields:
            if field not in nonRequiredFields:
                self.fields[field].required = True
        for field in ["email", "music_remark", "equipment_remark"]:
            self.fields[field].widget.attrs["class"] = "djedit-margin-bottom"
