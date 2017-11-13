# -*- coding: utf-8 -*-
import os
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from forms import ContactForm, DJEditForm
from .models import DJ
from .common import addDjContext, sendContactEmail as sendEmail


SHOW_MAINTENANCE_PAGE = ".qmail-maintenance"


def debug(s):
    if False:
        print ">>>>", s


def copyright(request):
    return render(request, "copyright.html")


def index(request):
    home = os.path.expanduser("~")
    if not os.path.exists(os.path.join(home, SHOW_MAINTENANCE_PAGE)):
        orderBy = ["country", "namesort"]
        djL = DJ.objects.order_by(*orderBy).filter(number_of_milongas__gte=1)
        context = {"djList": djL}
        addDjContext(request, DJ, context)
        return render(request, "index.html", context)
    return render(request, "index_empty.html")


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        firstname = request.POST.get("contact_firstname", '')
        lastname = request.POST.get("contact_lastname", '')
        email = request.POST.get("contact_email", '')
        content = request.POST.get("contact_content", '')
        magic = request.POST.get("contact_magic", '')
        if form.is_valid():
            email = sendEmail(firstname, lastname, email, content, magic)
            return redirect("contactfeedback")
        form = form_class()
        form.fields["contact_firstname"].initial = firstname
        form.fields["contact_lastname"].initial = lastname
        form.fields["contact_email"].initial = email
        form.fields["contact_content"].initial = content
        form.fields["contact_magic"].initial = magic
        return render(request, "contact_failed.html", {"form": form, })
    return render(request, "contact.html", {"form": form_class, })


def contactfeedback(request):
    context = {}
    addDjContext(request, DJ, context)
    return render(request, "contactfeedback.html", context)


def about(request):
    context = {}
    addDjContext(request, DJ, context)
    return render(request, "about.html", context)


def todo(request):
    context = {}
    addDjContext(request, DJ, context)
    return render(request, "todo.html", context)


def loginredirect(request):
    if request.user.is_authenticated():
        user = request.user
        if user.id == 1:  # admin MUST use admin URL
            # return HttpResponseRedirect(reverse("admin:index"))
            return contact(request)
        else:
            dj = DJ.objects.get(user=user)
            if dj and dj.number_of_milongas and dj.name:
                return djdetail(request, dj.id)
            return djedit(request)
    # This should not happen
    return index(request)


def customlogout(request):
    model_changed = False
    if not model_changed:
        logout(request)
        return index(request)


def djdetail(request, dj_id):
    dj = get_object_or_404(DJ, pk=dj_id)
    return render(request, "djdetail.html", {"dj": dj})


def djedit(request):
    if request.user.is_authenticated():
        debug("djedit called")
        html = "djedit.html"
        user = request.user
        djobject = DJ.objects.get(user=user)
        debug("djedit %s selected" % djobject)

        if request.method == 'POST':
            debug("djedit POST")
            djform = DJEditForm(request.POST, instance=djobject)
            djform.set_namesort(request)
            if djform.is_valid():
                debug("djedit form valid => save()")
                djform.save()
                html = "djdetail.html"
            else:
                debug("djedit form not valid")
        else:
            debug("djedit GET")
            djform = DJEditForm(instance=djobject)

        context = {"form": djform, "user": user}
        addDjContext(request, DJ, context)
        return render(request, html, context)

    # This should not happen!
    return index(request)
