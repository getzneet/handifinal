# handifinal

English below 
---
### Version française
Ceci est le dépot du projet menet dans le cadre de l'UE multiple forme du métier au sein du master sciences cognitives de l'université de Bordeaux. 

Ce site fonctionne avec Django. 
Si vous ne connaissez rien à la programmation vous pouvez suivre ce tutoriel de DjangoGirl https://tutorial.djangogirls.org
qui vous permet d'apprendre à concevoir et maitriser Django. 
Si vous savez programmer, partez directement sur le tuto Django https://www.djangoproject.com/start/

Pour développer et rendre accessible le site au public, utilisez https://www.pythonanywhere.com qui permet d'héberger gratuitement le site. (suivre ces instructions pour installer le site https://tutorial.djangogirls.org/en/deploy/)

Le template (autrement dit le design du site) a été réalisé avec bootstrap. http://getbootstrap.com

---
### ENglish

This is the project's repository of a site dedicated to list hardware and software for personn with dissabilities. This site has been develop during "multiple forme du métier" course within the cognitive science degree at the University of Bordeaux.

This site has been made with love... by Django.
If you don't know anything about programming, you can follow this DjangoGirl's tutorial https://tutorial.djangogirls.org
which allows you to learn to design a website with Django.
If you know how to code, goto Django tutorial https://www.djangoproject.com/start/

In order to push this website online, use https://www.pythonanywhere.com to host it for free. (follow these instructions to install the site https://tutorial.djangogirls.org/en/deploy/)

The template was made with bootstrap. http://getbootstrap.com


# Développement web:
#### Fonctionnement basique du framework python Django




---

### Menu vu par l'utilisateur
![](https://i.imgur.com/9YB6gxj.png)

### Code html (template)
```html
...
<a href="/home">Accueil</a>
...
```


---
## URL

On associe une requête vers une adresse à une fonction.
```python

url('/home', home)
```

---

## Views

```python

def home(request):
	
    # récupérer les technologies dans la base de données
    technos = Technology.objects.all()
    
    # générer une page html et la renvoyer à l'utilisateur
    return render(
    	     request,
            'home.html',
            {'technos': technos}
    )
```

---

## Models

```python
from django.db import models


class Technology(models.Model):

    """
    modèle de technologie
    une instance de ce modèle == une ligne dans la bdd
    un attribut == une colonne dans la bdd
    
    """
    
    nom = models.Charfield()
    prix = models.IntergerField()
    ...
    
```
---
## Démonstration des fonctionnalités du site

---


# Pour aller plus loin

* Améliorer l'accessibilité : Text to speech, contrastes élévés...
* Améliorer la fonction de recherche (code commenté)
* Trouver un hébergement viable
* Vérifier les vidéos associées aux technologies
* Ajouter des images pour les technologies existantes


