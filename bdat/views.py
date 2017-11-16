import logging as log
import urllib.request
import urllib.parse
import re

from django.shortcuts import render_to_response, render
from .models import Technology
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import SubmissionForm


def technology(request, id):

    """
    render
    a technology
    """

    techno = Technology.objects.get(id=int(id))

    if not techno.video:

        log.debug("No video found for techno '{}', running youtube lookup...".format(techno.nom))
        techno.video = Utils.get_technology_video(techno.nom)
        techno.save(update_fields=['video'])

    return render(request, "techno.html", {"att": techno})


def search(request, words):

    """
    search
    """

    words = request.GET["q"].split(" ")
    search_results = Utils.search_in_objects(words)

    return render(
        request,
        "list.html",
        {'attributs': search_results, 'n_results': len(search_results), 'words': " ".join(words)}
    )


def home(request):

    """
    home page

    """

    queryset = Technology.objects.filter(show=1)

    return render(request, "home.html", {'attributs': queryset, 'words': 0, 'n_results': 0})


def categories(request):

    """
    categories page
    """

    return render_to_response("categories.html")


def about(request):

    """
    about page
    """

    return render_to_response("about.html")


def contact(request):

    """
    contact page
    """

    return render_to_response("contact.html")


def subform(request):

    """
    renders the form page
    """

    if request.method == "POST":

        form = SubmissionForm(request.POST, request.FILES)

        if form.is_valid():
            return render(request, "subform.html", {'form': form, 'success': 1})

        else:
            return render(request, "subform.html", {'form': form, 'success': 0})

    else:

        form = SubmissionForm()

    return render(request, "subform.html", {'form': form, 'success': 0})


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


def category(request):
    queryset = Utils.get_all_technologies()

    return render(request,
        "category.html",
        {"attributs": [entry.type_techno for entry in queryset], "titre": "Assistance", "nb_attributs": len(queryset)}
    )

    # ---------------------------- Utils --------------------------------------------------------------- #

class Utils:

    @staticmethod
    def get_all_technologies():
        return list(Technology.objects.all())

    @staticmethod
    def search_in_objects(words):

        """
        search
        in techno's attributes
        (need to find a replacement)

        """

        technos = Utils.get_all_technologies()
        match = []

        for word in words:
            for techno in technos:
                attributes = Utils.get_techno_attributes(techno)
                for att in attributes:
                    if word.lower() in att:
                        if not techno in match and techno.show:
                            match.append(techno)

        return match

    @staticmethod
    def get_techno_attributes(techno):
        return [i.lower() for i in techno.__dict__.values() if type(i) == str]

    @staticmethod
    def get_technology_video(name):

        """
        not so great method to get a video
        describing the techno from youtube
        """

        query_string = urllib.parse.urlencode({"search_query": name})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return "http://www.youtube.com/embed/" + search_results[0]
