from django import forms
from django.db import models

from crispy_forms.bootstrap import Field, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout, Fieldset

from .models import Technology


class SubmissionForm(forms.Form):

    error_css_class = 'has-error'

    name = forms.CharField(
        max_length=30,
        label="Votre nom",
        required=False
    )

    email = forms.EmailField(
        max_length=254,
        label="Votre email",
        required=True
    )

    nom = forms.CharField(
        max_length=100,
        label="Nom de la technologie",
        required=True
    )

    prix = forms.DecimalField(
        label="Prix de la technologie", 
        required=False
    )

    age = forms.ChoiceField(
        widget=forms.Select,
        choices=[
         ('Tous âges', 'Tous âges'),
         ('Enfants', 'Enfants'),
         ('Adultes', 'Adultes'),
         ('Personnes âgées', 'Personnes âgées')
        ],
        label="Tranche d'âge concernée",
        required=True
    )

    cif = forms.ChoiceField(
        choices=[
            ('Organisation', 'Organisation'),
            ('Déplacement',' Déplacement'),
            ('Santé', 'Santé'),
            ('Vie domestique', 'Vie domestique'),
            ('Loisirs', 'Loisirs'),
            ('Vie sociale', 'Vie sociale'),
            ('Travail', 'Travail'),
            ('Apprentissage', 'Apprentissage')
        ],
        label="Classification",
        required=True
    )

    type_techno = forms.CharField(max_length=100, label="Type de technologie", required=False)
    activite = forms.CharField(max_length=100, label="Activité", required=False)
    source = forms.CharField(max_length=100, label="Source", required=False)
    article = forms.CharField(max_length=None, label="Article", required=False)
    entreprise = forms.CharField(max_length=100, label="Entreprise/Laboratoire", required=True)
    patho = forms.CharField(max_length=100, label="Pathologie", required=False)

    fonction = forms.CharField(max_length=100, label="Fonction", required=False)

    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='',
        required=True
    )
    
    video = forms.CharField(max_length=None, required=False)

    image = forms.ImageField(required=False)

    required_fields = ['nom', 'email', 'age', 'description', 'entreprise', 'cif'] 

    def __init__(self, *args):

        super().__init__(*args)

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset('Vos informations',
                Field('name', placeholder='Votre nom ici'),
                Field('email', placeholder='Votre email ici')
            ), Fieldset('Informations concernant la </br> </br> technologie',
                Tab('Informations obligatoires', 'nom', 'cif', 'age', 'entreprise', 'description'),
                Tab('Informations complémentaires', 'image', 'prix', 'source')
            )
        )

    def clean(self):

        """
        called by is_valid method
        when the form is going 
        to be validated
        """

        cleaned_data = super(SubmissionForm, self).clean()

        if not all(cleaned_data.get(field) for field in self.required_fields):

            raise forms.ValidationError(
                message="Vous devez remplir les champs marqués d'une étoile !",
            )

        else:

            # instantiate a new technoloy
            new = Technology()

            # don't show img on the website when added by form
            # (wait for an admin validation)
            new.show = False

            # set all forms attributes to 
            # technology model 
            for key in cleaned_data.keys():
                setattr(new, key, cleaned_data.get(key))
            
            new.save(force_insert=True)
