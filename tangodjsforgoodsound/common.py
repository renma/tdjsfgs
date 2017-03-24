import unicodedata
from django import forms
from django.core.exceptions import ValidationError


class TrickyField(forms.Field):

    _artists = [
        "anibaltroilo",
        "carlosdisarli",
        "darienzo"
        "disarli",
        "juandarienzo",
        "osvaldopugliese",
        "pugliese",
        "sarli",
        "troilo"
    ]

    def _stripAccents(self, val, encoding="utf-8"):
        try:
            val = unicode(val, encoding)
        except Exception:
            pass
        nkfd = unicodedata.normalize('NFKD', val)
        val = nkfd.encode('ASCII', 'ignore')
        return val

    def _createAz(self, val):
        val = self._stripAccents(val)
        val = "".join([c if c.isalnum() else '' for c in val])
        return val.strip()

    def validate(self, value):
        super(forms.Field, self).validate(value)
        val = self._createAz(value.lower())
        if not val or val not in self._artists:
            raise ValidationError("Artist not valid")
