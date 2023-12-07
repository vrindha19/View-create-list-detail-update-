from django.urls import path

from django.urls import path
from.views import ForgotCreate,ForgotList,ForgotDetailView,ForgotUpdateView,ForgotDeleteView

urlpatterns=[
     path('forgot/create',ForgotCreate.as_view() ,name='forgot_create'),
      path('forgot/list',ForgotList.as_view(),name='forgot_list'),
    path('forgot/detail/<int:pk>/',ForgotDetailView.as_view(),name='forgot_detail'),
    path('forgot/update/<int:pk>/',ForgotUpdateView.as_view(),name='forgot_update'),
    path('forgot/delete/<int:pk>/',ForgotDeleteView.as_view(),name='forgot_delete'),


]