from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

# # Create your views here.
from django.views.generic.edit import CreateView
# from django.views.generic.edit import UpdateView
# from django.views.generic.list import RegisterView
# from django.views.generic.detail import DetailView

from .models import RegisterModel

class Registercreate(CreateView):
    model = RegisterModel
    fields = ['name', 'username', 'email', 'password', 'confirmpassword']
    template_name='registerform_create.html'
    success_url='/success/'

# class RegisterList(RegisterView):
#       model= RegisterModel
#       template_name='login_list.html'
#       context_object_name='login_list'
