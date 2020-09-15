from django.db import models
from django import forms

# Create your models here.

class SignUp(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    adress = models.CharField(max_length=120)
    apt = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip = models.CharField(max_length=120)
    country = models.CharField(max_length=120)

class GoldModelForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = "__all__"
