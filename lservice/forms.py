from django import forms
from .models import Item,SubItem


class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'