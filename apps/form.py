from django import forms

from apps.models import People


class UserForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'