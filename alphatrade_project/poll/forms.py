from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

#from .models import Order

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']

class CreateMyPollForm(ModelForm):
    class Meta:
        model = MyPoll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four']

""" class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__' """

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']