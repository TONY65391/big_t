from django import forms
from . models import MODELS

class FORMS(forms.ModelForm):
    class Meta:
        model = MODELS
        fields = "__all__"