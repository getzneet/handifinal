import logging as log
import urllib.request
import urllib.parse
import re

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from .models import Institution, Technology


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

    if not hasattr(techno, "video"):
        log.debug("No video found for techno '{}', running youtube lookup...".format(techno.nom))
        techno.video = get_technology_video(techno.nom)

    return render(request, "techno.html",
                  {"att": techno})


def technology_(request):
    queryset = Technology.objects.all()

    return render(request, "techno.html",
                  {"att": queryset[0]})

def get_technology_video(name):
    """
    shitty method to get a video describing the techno from youtube
    """

    query_string = urllib.parse.urlencode({"search_query": name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return "http://www.youtube.com/embed/" + search_results[0]
