# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import DJ


def createval(x):
    return x if x else ""


def djdetail(request, dj_id):
    dj = get_object_or_404(DJ, pk=dj_id)
    return render(request, "djdetail.html", {"dj": dj})


def index(request):
    orderBy = ["country", "style", "since", "name"]
    djList = DJ.objects.order_by(*orderBy)
    context = {"djList": djList}
    return render(request, "index.html", context)
