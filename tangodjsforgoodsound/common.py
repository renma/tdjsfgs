# Time-stamp: <2018-03-16 05:51:40 rene>
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


def createDJContext(request, DJModel, context={}):
    context["dj"] = None
    if request.user.is_authenticated():
        try:
            dj = DJModel.objects.get(user=request.user.id)
            context["dj"] = dj
        except Exception:
            pass
    return context


def createEmailTo():
    if os.path.exists("/home/rene"):
        return ["rm@cumparsita.ch"]
    return ["contact@tangodjsforgoodsound.info"]


def sendAnEmail(first, last, emailFrom, content, magic,
                subject, title, djname, setReplyTo, setKnownUsers):
    if djname:
        emailContent = [
            "", title, "",
            "    First name : %s" % first,
            "    Last name  : %s" % last,
            "    DJ name    : %s" % djname,
            "    Email      : %s" % emailFrom,
            "    Orquesta   : %s" % magic, ""]
    else:
        emailContent = [
            "", title, "",
            "    First name : %s" % first,
            "    Last name  : %s" % last,
            "    Email      : %s" % emailFrom,
            "    Orquesta   : %s" % magic, ""]

    if not magic:
        emailContent = emailContent[:-2]
        emailContent.append("")

    emailTo = createEmailTo()

    if setKnownUsers == 1:
        knownDJs = DJ.objects.all().filter(email=emailFrom)
        if knownDJs:
            L = [stripAccents(dj.name) for dj in knownDJs]
            msg = "Known DJ(s) with this email address : %s."
            emailContent.append(msg % ", ".join(L))
        knownUsers = User.objects.all().filter(email=emailFrom)
        if knownUsers:
            L = ["%s %s" % (stripAccents(u.first_name),
                            stripAccents(u.last_name)) for u in knownUsers]
            msg = "Known User with this email address : %s"
            emailContent.append(msg % ", ".join(L))
        if knownDJs or knownUsers:
            emailContent.append("")
    elif setKnownUsers == 2:
        emailContent.append("This is a new user.")
    elif setKnownUsers == 3:
        emailContent.append("This is a deleted user.")

    if content:
        emailContent.extend([content, ""])
    emailContent.append("This message was sent to: %s" % emailTo)
    replyTo = emailFrom if setReplyTo else "contact@tangodjsforgoodsound.info"
    emailFrom = "contact@tangodjsforgoodsound.info"
    email = EmailMessage(subject,
                         "\n".join(emailContent),
                         emailFrom,
                         emailTo,
                         reply_to=[replyTo])
    email.send()
    print "Email sent to: %s" % emailTo


def sendContactEmail(first, last, emailFrom, content, magic):
    subject = "New contact request"
    title = "A new contact request was entered on the website:"
    dj = ''
    setReplyTo, setKnownUsers = True, 1
    sendAnEmail(first, last, emailFrom, content, magic, subject, title, dj,
                setReplyTo, setKnownUsers)


def sendRegistrationEmail(first, last, djname, emailFrom, content, magic):
    subject = "New registration "
    title = "A new registration was entered on the website:"
    setReplyTo, setKnownUsers = False, 2
    sendAnEmail(first, last, emailFrom, content, magic, subject, title, djname,
                setReplyTo, setKnownUsers)


def sendRegistrationDeletedEmail(first, last, djname, emailFrom):
    subject = "Registration deleted"
    title = "A user has deleted its registration"
    content, magic = '', ''
    setReplyTo, setKnownUsers = False, 3
    sendAnEmail(first, last, emailFrom, content, magic, subject, title, djname,
                setReplyTo, setKnownUsers)


def doesEmailExist(request, email):
    theUser = User.objects.filter(id=request.user.id)[0] if request else None
    if theUser:
        objects = User.objects.exclude(id=theUser.id).filter(email=email)
    else:
        objects = User.objects.filter(email=email)
    if objects:
        # print ">>> User email %s exists already" % email
        return True
    if theUser:
        objects = DJ.objects.exclude(user=theUser).filter(email=email)
    else:
        objects = DJ.objects.filter(email=email)
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
