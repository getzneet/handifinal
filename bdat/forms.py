from django import forms
from .models import Technology


class SubmissionForm(forms.Form):

    error_css_class = 'has-error'

    name = forms.CharField(max_length=30, label="Votre nom", required=False)
    email = forms.EmailField(max_length=254, label="Votre email", required=False)

    nom = forms.CharField(
        max_length=100,
        label="Nom de la technologie",
        required=True
    )

    prix = forms.DecimalField(label="Prix de la technologie", required=False)
    age = forms.CharField(max_length=100, label="Tranche d'âge concernée", required=False)
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
        required=False
    )

    def clean(self):

        cleaned_data = super(SubmissionForm, self).clean()

        nom = cleaned_data.get('nom')
        # age = cleaned_data.get('age')
        # cif = cleaned_data.get('cif')

        if not nom:

            raise forms.ValidationError("Vous devez remplir l'ensemble des champs !")

        else:

            new = Technology()
            new.show = 0

            for key in cleaned_data.keys():
                setattr(new, key, cleaned_data.get(key))

            new.save(force_insert=True)
