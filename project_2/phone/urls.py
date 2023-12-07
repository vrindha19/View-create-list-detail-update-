from django.urls import path
from.views import LoginCreate,LoginList,LoginDetailView,LoginUpdateView


urlpatterns=[
     path('login/create',LoginCreate.as_view() ,name='login_create'),
     path('login/list',LoginList.as_view(),name='login_list'),
     path('login/detail/<int:pk>/',LoginDetailView.as_view(),name='login_detail'),
     path('login/update/<int:pk>/',LoginUpdateView.as_view(),name='login_update'),
]