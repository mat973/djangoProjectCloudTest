from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Profile


class UserRegisterForm(forms.Form):
    variable = forms.IntegerField(
        label='Введите номер варианта',
        required=True,
    )
    text = forms.SlugField(
        label='Введите задание',
        required=True,
    )





    # some = forms.ModelChoiceField(queryset=User.objects.all())
    #
    #  class Meta:
    #      model = Tusk
    #     fields = ['username', 'password1', 'password2', 'email']
