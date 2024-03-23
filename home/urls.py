from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_update/', views.add_update, name='add_update'),
]
