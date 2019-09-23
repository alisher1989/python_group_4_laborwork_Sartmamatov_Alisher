from django import forms
from django.forms import widgets
from webapp.models import PRODUCT_CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Name')
    description = forms.CharField(max_length=3000, required=True, label='Description', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=PRODUCT_CATEGORY_CHOICES, required=False, label='Category')
    amount = forms.IntegerField(min_value=1, required=True)
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True)