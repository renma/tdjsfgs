# Time-stamp: <2024-09-12 08:30:08 rene>
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

import unicodedata
import inspect
import logging
import os

from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ContactForm, RegisterForm, DJEditForm, SubscriberPasswordForm
from .models import DJ
from .common import createDJContext, sendContactEmail, sendRegistrationEmail, \
    sendRegistrationDeletedEmail, sendWelcomeEmail


SHOW_MAINTENANCE_PAGE = "maintenancemode"
logger = logging.getLogger("tdjsfgs")


def log():
    caller = inspect.stack()[1][3]
    if caller == "index":
        caller = "DJs"
    logger.info("%s" % caller)


@login_required
def change_password(request):
    log()
    if request.method == "POST":
        form = SubscriberPasswordForm(request.POST)
        if form.is_valid():
            try:
                request.user.set_password(form.cleaned_data["new_password1"])
                request.user.save()
                update_session_auth_hash(request, request.user)  # Important!
                logger.info("Password for user %s set" % request.user)
            except Exception:
                # This should not happen
                logger.error("Oooops, unexcpected error in change_password")
                context = {"form": form}
                context = createDJContext(request, DJ, context)
                return render(request, "change_password.html", context)
            else:
                context = {"form": form}
                context = createDJContext(request, DJ, context)
                return render(request, "change_password_success.html", context)
    else:
        form = SubscriberPasswordForm()
    context = {"form": form}
    context = createDJContext(request, DJ, context)
    return render(request, "change_password.html", context)


def copyright(request):
    log()
    context = createDJContext(request, DJ)
    return render(request, "copyright.html", context)


def linkpage(request):
    log()
    context = createDJContext(request, DJ)
    return render(request, "linkpage.html", context)


def index(request):
    log()
    home = os.path.expanduser("~")
    if not os.path.exists(os.path.join(home, SHOW_MAINTENANCE_PAGE)):
        # orderBy = ["country", "namesort"]
        # djL = DJ.objects.order_by(*orderBy).filter(number_of_milongas__gte=1)
        djL = []
        D = {}
        for dj in DJ.objects.filter(number_of_milongas__gte=1):
            # TODO handle exception like Rene Maurer "El firulete"
            # TODO use the namesort field for this
            s = dj.name.lower().split()
            x = s[1] if s[0] in ["dj", "tj"] and len(s) > 1 else s[0]
            D[dj.country.name.lower() + x + str(dj.id)] = dj
        keys = list(D.keys())
        keys.sort()
        for k in keys:
            dj = D[k]
            if dj.name.lower().startswith("dj ") \
               or dj.name.lower().startswith("tj "):
                dj.name = dj.name[3:]
            # HACK!
            djFullLocation = "%s, %s" % (dj.country.name, dj.province)
            dj.province = djFullLocation
            djL.append(D[k])
        # for dj in djL:
        #     print dj, dj.country, dj.province, dj.country.name
        context = {"djList": djL}
        context = createDJContext(request, DJ, context)
        return render(request, "index.html", context)
    return render(request, "index_empty.html")


def contact(request):
    log()
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        firstname = request.POST.get("contact_firstname", '')
        lastname = request.POST.get("contact_lastname", '')
        email = request.POST.get("contact_email", '')
        content = request.POST.get("contact_content", '')
        magic = request.POST.get("contact_magic", '')
        if form.is_valid():
            email = sendContactEmail(firstname, lastname, email, content,
                                     magic)
            context = createDJContext(request, DJ)
            return redirect("contactfeedback")
        context = {"form": form}
        return render(request, "contact.html", context)
    context = {"form": form_class}
    context = createDJContext(request, DJ, context)
    return render(request, "contact.html", context)


def contactfeedback(request):
    log()
    context = createDJContext(request, DJ)
    return render(request, "contactfeedback.html", context)


def project(request):
    log()
    context = createDJContext(request, DJ)
    return render(request, "project.html", context)


def more(request):
    log()
    context = createDJContext(request, DJ)
    return render(request, "more.html", context)


def loginredirect(request):
    log()
    if request.user.is_authenticated:
        user = request.user
        logger.info("%s logged in" % user)
        if user.id == 1:
            return redirect("/admin")
        else:
            dj = DJ.objects.get(user=user)
            if dj:
                logger.info("DJ details: %s" % dj.name)
                return djdetail(request, dj.id)
    # This should not happen
    return index(request)


def customlogout(request):
    log()
    logger.info("Logout %s" % request.user)
    model_changed = False
    if not model_changed:
        logout(request)
        return index(request)


def djdetail(request, dj_id):
    log()
    dj = get_object_or_404(DJ, pk=dj_id)
    logger.info("DJ details: %s" % dj.name)
    return render(request, "djdetail.html", {"dj": dj})


def djedit(request):
    log()
    if request.user.is_authenticated:
        html = "djedit.html"
        user = request.user
        djobject = DJ.objects.get(user=user)
        logger.debug("djedit %s selected" % djobject)
        if request.method == 'POST':
            logger.debug("djedit POST")
            djform = DJEditForm(request.POST, instance=djobject)
            djform.set_namesort(request)
            djform.request = request
            if djform.is_valid():
                logger.debug("djedit form valid")
                try:
                    theUser = User.objects.all().filter(id=user.id)[0]
                except Exception:
                    theUser = None
                if theUser:
                    logger.debug("djedit user found")
                    loginAddress = djform.cleaned_data.get("useremail")
                    msg = "djedit saved djform for %s"
                    logger.info(msg % theUser.username)
                    djform.save()
                    if not loginAddress == theUser.username \
                       or not loginAddress == theUser.email:
                        msg = "New Username %s => %s"
                        logger.info(msg % (theUser.username, loginAddress))
                        msg = "New Useremail %s => %s"
                        logger.info(msg % (theUser.email, loginAddress))
                        msg = "djedit saved user data for %s"
                        logger.info(msg % theUser.username)
                        theUser.username = loginAddress
                        theUser.email = loginAddress
                        User.save(theUser)
                    html = "djdetail.html"
                else:
                    logger.debug("djedit user not found")
            else:
                logger.debug("djedit form not valid")
        else:
            logger.debug("djedit GET")
            djform = DJEditForm(instance=djobject)

        context = {"form": djform, "user": user}
        context = createDJContext(request, DJ, context)
        return render(request, html, context)

    # This should not happen!
    return index(request)


def djdelete(request):
    log()
    if request.user.is_authenticated:
        user = request.user
        try:
            theUser = User.objects.all().filter(id=user.id)[0]
        except Exception:
            theUser = None
        try:
            theDJ = DJ.objects.all().filter(user=user)[0]
        except Exception:
            theDJ = None
        logger.info("djdelete, DJ = %d %s" % (theDJ.id, theDJ))
        logger.info("djdelete, User = %d %s" % (theUser.id, theUser))
        if request.method == "POST" and theUser and theDJ:
            logout(request)
            logger.info("logged out user")
            theDJ.delete()
            logger.debug("DJ deleted")
            theUser.delete()
            logger.debug("User deleted")
            sendRegistrationDeletedEmail(theUser.first_name, theUser.last_name,
                                         theDJ.name, theUser.email)
            return render(request, "djdeleted.html")
        context = {"user": user}
        context = createDJContext(request, DJ, context)
        return render(request, "djdelete.html", context)
    return index(request)


def djdeleted(request):
    log()
    return render(request, "djdeleted.html")


def register(request):
    log()
    form_class = RegisterForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        firstname = request.POST.get("register_firstname", '')
        lastname = request.POST.get("register_lastname", '')
        djname = request.POST.get("register_djname", '')
        email = request.POST.get("register_email", '')
        password1 = request.POST.get("register_password1", '')
        # password2
        magic = request.POST.get("register_magic", '')
        if form.is_valid():
            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                username=email,
                email=email,
                password=password1)
            dj = DJ(user=user,
                    useremail=email,
                    name=djname,
                    number_of_milongas=0)
            dj.save()
            retval = sendWelcomeEmail(firstname, lastname, djname, email)
            if retval == 1:
                sendRegistrationEmail(firstname, lastname, djname, email,
                                      "Welcome email sent to %s" % email,
                                      magic)
            else:
                sendRegistrationEmail(firstname, lastname, djname, email,
                                      "ERROR sending email to %s" % email,
                                      magic)
            return redirect("registered")
        return render(request, "registration/register.html", {"form": form, })
    return render(request, "registration/register.html",
                  {"form": form_class, })


def registered(request):
    log()
    return render(request, "registration/registered.html")


def technology(request):
    log()
    home = os.path.expanduser("~")
    if not os.path.exists(os.path.join(home, SHOW_MAINTENANCE_PAGE)):
        orderBy = ["computer", "player", "namesort"]
        djL = DJ.objects.order_by(*orderBy).filter(number_of_milongas__gte=1)
        for dj in djL:
            if dj.name.lower().startswith("dj ") \
               or dj.name.lower().startswith("tj "):
                dj.name = dj.name[3:]
        context = {"djList": djL}
        context = createDJContext(request, DJ, context)
        return render(request, "technology.html", context)
    return render(request, "index_empty.html")


@login_required
def logfile(request):

    def stripAccents(val, encoding="utf-8"):
        nfkd_form = unicodedata.normalize('NFKD', val)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

    log()
    name = "%s %s" % (request.user.first_name, request.user.last_name)
    if name in ["Rene Maurer", "Albert Alt"]:
        lines = []
        """
        import codecs
        with codecs.open("tdjsfgs.log", "r", encoding="utf-8") as f:
            lines = f.readlines()
            lines.reverse()
        """
        lines.append("\n\n    The logfile is only available on the server.")
        lines.append("\n\n    Location: ~/ALL/mysite/tdjsfgs.log [.*]")
        content = stripAccents("".join(lines))
        return HttpResponse(content, content_type="text/plain")
    return HttpResponse("", content_type="text/plain")
