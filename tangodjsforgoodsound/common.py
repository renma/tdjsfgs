import os
import unicodedata
from django import forms
from django.core.mail import EmailMessage


def createEmailTo():
    if os.path.exists("/home/tdjsfgs"):
        return ["contact@tangodjsforgoodsound"]
    if os.path.exists("/home/rene"):
        return ["rm@cumparsita.ch"]
    return ["rm@cumparsita.ch", "saludos@bluewin.ch"]


def sendContactEmail(first, last, emailFrom, content, magic):
    emailTo = createEmailTo()
    emailContent = [
        "", "A new contact request was entered on the website:", "",
        "    First name : %s" % first,
        "    Last name  : %s" % last,
        "    Email      : %s" % emailFrom,
        "    Orquesta   : %s" % magic, ""]
    if content:
        emailContent.extend([content, ""])
    emailContent.append("This message was sent to: %s" % emailTo)
    replyTo = emailFrom
    emailFrom = "website@tangodjsforgoodsound.cumparsita.ch"
    email = EmailMessage("New contact request",
                         "\n".join(emailContent),
                         emailFrom,
                         emailTo,
                         reply_to=[replyTo])
    email.send()
    print "Email sent to: %s" % emailTo


class TrickyField(forms.Field):

    _artists = [
        "anibaltroilo",
        "carlosdisarli",
        "darienzo",
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
        super(TrickyField, self).validate(value)
        val = self._createAz(value.lower())
        if value and val not in self._artists:
            print "This artist isn't valid: %s" % val
            raise forms.ValidationError(("Artist not valid"), code="invalid")
