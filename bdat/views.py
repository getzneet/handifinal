import logging as log
import urllib.request
import urllib.parse
import re
from render_block import render_block_to_string

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from .models import Institution, Technology


# def get_all_technologies():
    
    # data = []

    # for tech in Technology.objects.all():

        # data.append({
          # "name": tech.name, 
          # "description": tech.description,
          # "entreprise":tech.entreprise,
          # "type_techno": tech.type_techno,
          # "video": tech.video,
          # "article": tech.article,
          # "age": tech.age
          # })

    # return data
def get_all_technologies():
    return list(Technology.objects.all())


def home(request):
    queryset = get_all_technologies()

    return render(request, "home.html", {'attributs': queryset})


def category(request):
    queryset = get_all_technologies()

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
    queryset = get_all_technologies()

    return render(request, "category.html",
                  {"attributs": [entry.type_techno for entry in queryset], "titre": "Assistance",
                   "nb_attributs": len(queryset)})


def categoryf(request):
    queryset = get_all_technologies()

    return render(request, "category.html",
                  {"attributs": [entry.fonction for entry in queryset], "titre": "Fonctions",
                   "nb_attributs": len(queryset)})


def categoryt(request):
    queryset = get_all_technologies()

    return render(request, "category.html",
                  {"attributs": [entry.nom for entry in queryset], "titre": "Technologies",
                   "nb_attributs": len(queryset)})


def technology(request, idx):

    techno = Technology.objects.get(idx=int(idx))
    
    if techno.video is None:
        log.debug("No video found for techno '{}', running youtube lookup...".format(techno.nom))
        techno.video = get_technology_video(techno.nom)
        
        if techno.video is not None:
            techno.save()

    return render(request, 
                  "techno.html",
                  {"att": techno})


def search(request, words):
    
    if hasattr(request, 'GET'):
        if "q" in request.GET.keys():
            words = request.GET["q"]

            search_results = search_in_objects(words)

            return render(request, 
                    "home.html",
                   {'attributs': search_results})


def search_in_objects(*words):
    
    technos = get_all_technologies()
    match = []

    for w in words:
        for techno in technos:
            att = [i.lower() for i in techno.__dict__.values() if type(i) == str]
            for a in att:
                if w.lower() in a:
                    if not techno in match:
                        match.append(techno)

    return match

def get_technology_video(name):
    """
    shitty function to get a video describing the techno from youtube
    """

    query_string = urllib.parse.urlencode({"search_query": name})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return "http://www.youtube.com/embed/" + search_results[0]
