# -*- coding: utf-8 -*-
import os
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from forms import ContactForm, DJEditForm
from .models import DJ
from .common import sendContactEmail


def createEmailTo():
    if os.path.exists("/home/rene"):
        return ["rm@cumparsita.ch"]
    return ["rm@cumparsita.ch", "saludos@bluewin.ch"]


def createval(x):
    return x if x else ""


def djdetail(request, dj_id):
    dj = get_object_or_404(DJ, pk=dj_id)
    return render(request, "djdetail.html", {"dj": dj})


def djedit(request):
    if request.user.is_authenticated():
        html = "djedit.html"
        user = request.user
        data = DJ.objects.get(user=user)
        if request.method == 'POST':
            djform = DJEditForm(request.POST, instance=data)
            if djform.is_valid():
                djform.save()
                html = "djedit_saved.html"
        else:
            data = DJ.objects.get(user=user)
            djform = DJEditForm(instance=data)
        return render(request, html, {"form": djform, "user": user})
    # This should not happen!
    return index(request)


def index(request):
    orderBy = ["country", "style", "since", "name"]
    djList = DJ.objects.order_by(*orderBy).filter(number_of_milongas__gte=1)
    context = {"djList": djList}
    return render(request, "index.html", context)


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            firstName = request.POST.get("contact_firstname", '')
            lastName = request.POST.get("contact_lastname", '')
            email = request.POST.get("contact_email", '')
            content = request.POST.get("contact_content", '')
            magic = request.POST.get("contact_magic", '')
            emailTo = createEmailTo()
            email = sendContactEmail(firstName, lastName, email, emailTo,
                                     content, magic)
            return redirect("contactfeedback")
        else:
            return render(request, "contact_failed.html")
    return render(request, "contact.html", {"form": form_class, })


def contactfeedback(request):
    return render(request, "contactfeedback.html")


def about(request):
    return render(request, "about.html")


def todo(request):
    return render(request, "todo.html")
