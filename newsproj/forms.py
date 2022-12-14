from django import forms
from django.core.exceptions import ValidationError
from .models import New, Category, NewCategory, Author
from django.forms import ModelForm


class NewForm(forms.ModelForm):
    description = forms.CharField(min_length=5)

    class Meta:
        model = New
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")
        author = cleaned_data.get("author")


        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

            return cleaned_data

