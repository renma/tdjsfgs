# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from forms import ContactForm, DJEditForm
from .models import DJ
from .common import sendContactEmail as sendEmail


def index(request):
    orderBy = ["country", "namesort"]
    djList = DJ.objects.order_by(*orderBy).filter(number_of_milongas__gte=1)
    context = {"djList": djList}
    return render(request, "index.html", context)


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
    return render(request, "contactfeedback.html")


def about(request):
    return render(request, "about.html")


def todo(request):
    return render(request, "todo.html")


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
            djform.set_namesort(request)
            if djform.is_valid():
                djform.save()
                html = "djedit_saved.html"
        else:
            data = DJ.objects.get(user=user)
            djform = DJEditForm(instance=data)
        return render(request, html, {"form": djform, "user": user})
    # This should not happen!
    return index(request)
