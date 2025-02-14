from django import forms
from myapp7.models import myapp7Model


class myapp7Form(forms.ModelForm):
    class Meta:
        model = myapp7Model
        fields = "__all__"
