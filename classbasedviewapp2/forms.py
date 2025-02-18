from django import forms
from classbasedviewapp2.models import SuModel


class SuForm(forms.ModelForm):
    class Meta:
        model = SuModel
        fields = "__all__"