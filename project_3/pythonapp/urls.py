from django.urls import path
from.views import Registercreate,RegisterList,RegisterDetailView,RegisterUpdateView,RegisterDeleteView
# LoginList,LoginDetailView,LoginUpdateView


urlpatterns=[
     path('register/create',Registercreate.as_view() ,name='register_create'),
      path('register/list',RegisterList.as_view(),name='register_list'),
     path('register/detail/<int:pk>/',RegisterDetailView.as_view(),name='register_detail'),
     path('register/update/<int:pk>/',RegisterUpdateView.as_view(),name='register_update'),
    path('register/delete/<int:pk>/',RegisterDeleteView.as_view(),name='register_delete'),
     
]