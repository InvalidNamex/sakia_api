# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('getItemsList/', views.getItemsList),
    path('getItemsClassList/', views.getItemsClassList),
    path('createUser/', views.create_user),
    path('getUsersList/', views.get_mobile_end_users),
]
