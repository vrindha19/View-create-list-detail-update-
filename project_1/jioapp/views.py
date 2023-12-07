from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render

# # # Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import ForgotModel

class ForgotCreate(CreateView):
      model=ForgotModel

      fields=['Email']
      template_name='forgot.html'
      success_url='/success/'


from.models import ForgotModel

class ForgotList(ListView):
    model=ForgotModel

    template_name='forgot list.html'
    context_object_name='forgot_list'


class ForgotDetailView(DetailView):
      model= ForgotModel
      template_name='forgotform_detail.html'
      context_object_name='forgot_Model'

class ForgotUpdateView(UpdateView):
    model = ForgotModel  # Specify your model
    template_name = 'forgotform_update.html' 
    success_url='/success/' # Specify your template name
    fields = '__all__'  # Use '__all__'     

class ForgotDeleteView(DeleteView) :  
      model=ForgotModel
      template_name='forgotform_delete.html'
      success_url = reverse_lazy('forgot_list')

      def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)  
            context['Email'] = 'confirm delete forgot object'
            return context 
