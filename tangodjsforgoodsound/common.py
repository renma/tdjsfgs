# Time-stamp: <2018-03-09 21:26:08 rene>
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

import os
import unicodedata
from django import forms
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .models import DJ


USEREMAIL_NOT_REGISTERED = "USEREMAIL_NOT_REGISTERED"


def stripAccents(val, encoding='utf-8'):
    try:
        assert(unicode(val, encoding))
        val = unicode(val, encoding)
    except TypeError:
        pass
    nkfd = unicodedata.normalize('NFKD', val)
    val = nkfd.encode('ASCII', 'ignore')
    return val


def addDjContext(request, DJModel, context):
    context["dj"] = None
    if request.user.is_authenticated():
        try:
            dj = DJModel.objects.get(user=request.user.id)
            context["dj"] = dj
        except Exception:
            pass


def createEmailTo():
    if os.path.exists("/home/rene"):
        return ["rm@cumparsita.ch"]
    return ["contact@tangodjsforgoodsound.info"]


def sendContactEmail(first, last, emailFrom, content, magic):
    emailTo = createEmailTo()
    emailContent = [
            "", "A new contact request was entered on the website:", "",
            "    First name : %s" % first,
            "    Last name  : %s" % last,
            "    Email      : %s" % emailFrom,
            "    Orquesta   : %s" % magic, ""]

    knownDJs = DJ.objects.all().filter(email=emailFrom)
    if knownDJs:
        L = [stripAccents(dj.name) for dj in knownDJs]
        msg = "Known DJ(s) with this email address : %s"
        emailContent.append(msg % ", ".join(L))
    knownUsers = User.objects.all().filter(email=emailFrom)
    if knownUsers:
        L = ["%s %s" % (stripAccents(u.first_name),
                        stripAccents(u.last_name)) for u in knownUsers]
        msg = "Known User with this email address : %s"
        emailContent.append(msg % ", ".join(L))
    if knownDJs or knownUsers:
        emailContent.append("")
    if content:
        emailContent.extend([content, ""])
    emailContent.append("This message was sent to: %s" % emailTo)
    replyTo = emailFrom
    emailFrom = "contact@tangodjsforgoodsound.info"
    email = EmailMessage("New contact request",
                         "\n".join(emailContent),
                         emailFrom,
                         emailTo,
                         reply_to=[replyTo])
    email.send()
    print "Email sent to: %s" % emailTo


def doesEmailExist(request, email):
    theUser = User.objects.filter(id=request.user.id)[0]
    objects = User.objects.exclude(id=theUser.id).filter(email=email)
    if objects:
        # print ">>> User email %s exists already" % email
        return True
    objects = DJ.objects.exclude(user=theUser).filter(email=email)
    if objects:
        # print ">>> Global email %s exists already" % email
        return True
    return False

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

    def _createAz(self, val):
        val = stripAccents(val)
        val = "".join([c if c.isalnum() else '' for c in val])
        return val.strip()

    def validate(self, value):
        super(TrickyField, self).validate(value)
        val = self._createAz(value.lower())
        if value and val not in self._artists:
            print "This artist isn't valid: %s" % val
            raise forms.ValidationError(("Artist not valid"), code="invalid")
