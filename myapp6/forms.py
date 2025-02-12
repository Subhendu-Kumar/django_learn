from django import forms


class skForm(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=20)
    age = forms.IntegerField()
