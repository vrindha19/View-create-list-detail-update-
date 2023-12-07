from django.urls import path
from.views import Registercreate
# LoginList,LoginDetailView,LoginUpdateView


urlpatterns=[
     path('register/create',Registercreate.as_view() ,name='register_create'),
    #  path('register/list',RegisterList.as_view(),name='register_list'),
    #  path('login/detail/<int:pk>/',LoginDetailView.as_view(),name='login_detail'),
    #  path('login/update/<int:pk>/',LoginUpdateView.as_view(),name='login_update'),
]