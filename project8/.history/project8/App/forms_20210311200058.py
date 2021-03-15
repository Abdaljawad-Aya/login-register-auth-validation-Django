from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import form
from .models import Order


class OrderForm(ModelForm):
  class Meta:
    model = Order
    fields = '__all__'