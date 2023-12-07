from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

# # Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import LoginModel

class LoginCreate(CreateView):
      model=LoginModel
      fields=['username','password']
      template_name='login_form.html'
      success_url='/success/'


class LoginList(ListView):
      model= LoginModel
      template_name='login_list.html'
      context_object_name='login_list'

class LoginDetailView(DetailView):
      model= LoginModel
      template_name='login_detail.html'
      context_object_name='login_Model'

class LoginUpdateView(UpdateView):
    model = LoginModel  # Specify your model
    template_name = 'login_update.html' 
    success_url='/success/' # Specify your template name
    fields = '__all__'  # Use '__all__'     
      



      
