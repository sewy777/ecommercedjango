# created forms.py in users after making models for esewa

from dataclasses import field,fields
from django import forms
from django.forms import ModelForm

from .models import Order

class Orderform(ModelForm):
    class Meta:
        model=Order
        fields=['quantity' ,'contact_no','address','payment_method']