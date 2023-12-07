from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

# # Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
# from django.views.generic.list import RegisterView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import RegisterModel

class Registercreate(CreateView):
    model = RegisterModel
    fields = ['name', 'username', 'email', 'password', 'confirmpassword']
    template_name='registerform_create.html'
    success_url='/success/'

class RegisterList(ListView
                   ):
      model= RegisterModel
      template_name='registerform_list.html'
      context_object_name='register_list'

class RegisterDetailView(DetailView):
      model= RegisterModel
      template_name='registerform_detail.html'
      context_object_name='register_Model'

class RegisterUpdateView(UpdateView):
    model = RegisterModel  # Specify your model
    template_name = 'registerform_update.html' 
    success_url='/success/' # Specify your template name
    fields = '__all__'  # Use '__all__'     

class RegisterDeleteView(DeleteView) :  
      model=RegisterModel
      template_name='registerform_delete.html'
      success_url = reverse_lazy('register_list')

      def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)  
            context['name'] = 'confirm delete login object'
            return context 

