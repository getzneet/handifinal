from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from .models import Institution, Technology
import logging as log


# Create your views here.

def home(request):
    queryset = Technology.objects.all()
    return render(request, "home.html", {'attributs': list(queryset)})


def category(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.type_techno for entry in queryset], "titre": "Assistance",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def categories(request):
    return render_to_response("categories.html")


def about(request):
    return render_to_response("about.html")


def contact(request):
    return render_to_response("contact.html")


def categorya(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.type_techno for entry in queryset], "titre": "Assistance",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def categoryf(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.fonction for entry in queryset], "titre": "Fonctions",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def categoryt(request):
    queryset = Technology.objects.all()

    return render(request, "category.html",
                  {"attributs": [entry.nom for entry in queryset], "titre": "Technologies",
                   "nb_attributs": [entry for entry in queryset].__len__()})


def technology(request, idx):
    queryset = Technology.objects.all()
    techno = [techno for techno in queryset if techno.idx == int(idx)][0]

    return render(request, "techno.html",
                  {"att": techno})


def technology_(request):
    queryset = Technology.objects.all()

    return render(request, "techno.html",
                  {"att": queryset[0]})
