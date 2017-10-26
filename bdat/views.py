import logging as log
import urllib.request
import urllib.parse
import json
import re

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from .models import Institution, Technology
from django.http import JsonResponse


def categories(request):
    return render_to_response("categories.html")


def about(request):
    return render_to_response("about.html")


def contact(request):
    return render_to_response("contact.html")

def subform(request):
    return render_to_response("subform.html")

def categorya(request):
    queryset = Utils.get_all_technologies()

    return render(request, "category.html",
                  {"attributs": [entry.type_techno for entry in queryset], "titre": "Assistance",
                   "nb_attributs": len(queryset)})


def categoryf(request):
    queryset = Utils.get_all_technologies()

    return render(request, "category.html",
                  {"attributs": [entry.fonction for entry in queryset], "titre": "Fonctions",
                   "nb_attributs": len(queryset)})


def categoryt(request):
    queryset = Utils.get_all_technologies()

    return render(request, "category.html",
                  {"attributs": [entry.nom for entry in queryset], "titre": "Technologies",
                   "nb_attributs": len(queryset)})

def home(request):
    queryset = Utils.get_all_technologies()

    return render(request, "home.html", {'attributs': queryset, 'words': 0, 'n_results': 0})


def category(request):
    queryset = Utils.get_all_technologies()

    return render(request, "category.html",
                  {"attributs": [entry.type_techno for entry in queryset], "titre": "Assistance",
                   "nb_attributs": len(queryset)})


def technology(request, idx):

    techno = Technology.objects.get(idx=int(idx))
    
    if techno.video is None:

        log.debug("No video found for techno '{}', running youtube lookup...".format(techno.nom))
        techno.video = Utils.get_technology_video(techno.nom)
        techno.save(update_fields=['video'])

    return render(request, "techno.html", {"att": techno})


def search(request, words):
    
        words = request.GET["q"].split(" ")
        search_results = Utils.search_in_objects(words)

        return render(request,
            "list.html", 
            {'attributs': search_results, 'n_results': len(search_results), 'words': " ".join(words)})         
                
    # ---------------------------- Utils --------------------------------------------------------------- # 

class Utils:

    @staticmethod 
    def get_all_technologies():
        return list(Technology.objects.all())

    @staticmethod 
    def search_in_objects(words):
        
        technos = Utils.get_all_technologies()
        match = []

        for w in words:
            for techno in technos:
                att = [i.lower() for i in techno.__dict__.values() if type(i) == str]
                for a in att:
                    if w.lower() in a:
                        if not techno in match:
                            match.append(techno)

        return match

    @staticmethod
    def get_technologies_att(technos):
    
        data = []

        for tech in technos:

            data.append({
              "nom": tech.nom,
              "description": tech.description,
              "entreprise":tech.entreprise,
              "type_techno": tech.type_techno,
              "video": tech.video,
              "article": tech.article,
              "age": tech.age,
              "patho": tech.patho,
              "cif": tech.cif,
              })

        return data

    @staticmethod
    def get_technology_video(name):
        """
        shitty function to get a video describing the techno from youtube
        """

        query_string = urllib.parse.urlencode({"search_query": name})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return "http://www.youtube.com/embed/" + search_results[0]
