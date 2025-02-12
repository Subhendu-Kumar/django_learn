from django import forms
from django.core import validators


def start_with_s(value):
    if value[0] != "s":
        raise forms.ValidationError("name must start with letter s")


class employeeForm(forms.Form):
    name = forms.CharField(max_length=20, validators=[start_with_s])
    city = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=20)
    age = forms.IntegerField()
    password = forms.CharField()
    retypepassword = forms.CharField()

    def clean(self):
        super().clean()
        pwd = self.cleaned_data["password"]
        rpwd = self.cleaned_data["retypepassword"]
        if pwd != rpwd:
            raise forms.ValidationError("password mismatch!!")

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 6:
            raise forms.ValidationError("name must be 6 char long atleast")
        return name
