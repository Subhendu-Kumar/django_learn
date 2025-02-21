from django import forms
from crudmysqlapp.models import user


class user_form(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"
