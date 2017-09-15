from django import forms
from . common import TrickyField


class ContactForm(forms.Form):

    contact_firstname = forms.CharField(required=True)
    contact_lastname = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    attrs = {'rows': 4, 'cols': 30}
    contact_content = forms.CharField(required=False,
                                      widget=forms.Textarea(attrs=attrs))
    contact_magic = TrickyField(required=True)
    contact_lossless = forms.BooleanField(required=True)
    contact_scard = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_firstname'].label = "Your first name"
        self.fields['contact_lastname'].label = "Your family name"
        self.fields['contact_email'].label = "Your email address"
        self.fields['contact_content'].label = "Your message"
        self.fields['contact_magic'].label = "One of the big four orchestras"
        self.fields['contact_lossless'].label = "I don't play lossy formats"
        self.fields['contact_scard'].label = "I use good quality soundcards"
