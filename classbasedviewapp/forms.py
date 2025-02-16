from django import forms

class myForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()