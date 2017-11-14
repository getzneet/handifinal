from django import forms

from crispy_forms.bootstrap import Field, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout, Fieldset

from .models import Technology


class SubmissionForm(forms.Form):

    error_css_class = 'has-error'

    name = forms.CharField(max_length=30, label="Votre nom", required=False)
    email = forms.EmailField(max_length=254, label="Votre email", required=True)

    nom = forms.CharField(
        max_length=100,
        label="Nom de la technologie",
        required=True
    )

    prix = forms.DecimalField(label="Prix de la technologie", required=True)
    age = forms.CharField(max_length=100, label="Tranche d'âge concernée", required=True)
    type_techno = forms.CharField(max_length=100, label="Type de technologie", required=False)
    activite = forms.CharField(max_length=100, label="Activité", required=False)
    source = forms.CharField(max_length=100, label="Source", required=False)
    article = forms.CharField(max_length=None, label="Article", required=False)
    entreprise = forms.CharField(max_length=100, label="Entreprise", required=False)
    patho = forms.CharField(max_length=100, label="Pathologie", required=False)
    cif = forms.CharField(max_length=100, label="Classification CIF", required=False)
    fonction = forms.CharField(max_length=100, label="Fonction", required=False)
    video = forms.CharField(max_length=None, required=False)

    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='',
        required=True
    )

    required_fields = ['nom', 'email', 'age', 'description', 'prix']

    def __init__(self, *args):

        super().__init__(*args)

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Fieldset('Vos informations',
                    Field('name', placeholder='Votre nom ici'),
                    Field('email', placeholder='Votre email ici')
            ),
            Fieldset('Informations concernant la </br> </br> technologie',
                TabHolder(
                    Tab('Informations obligatoires', 'nom', 'prix', 'age', 'description'),
                    Tab('Informations complémentaires', 'patho', 'cif', 'entreprise', 'source')
                )
            )
        )

    def clean(self):

        cleaned_data = super(SubmissionForm, self).clean()

        if not all(cleaned_data.get(field) for field in self.required_fields):

            raise forms.ValidationError(
                    message="Vous devez remplir les champs marqués d'une étoile !",
            )

        else:

            new = Technology()
            new.show = 0

            for key in cleaned_data.keys():
                setattr(new, key, cleaned_data.get(key))

            new.save(force_insert=True)
