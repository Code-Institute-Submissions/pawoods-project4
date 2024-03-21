from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('wish_list/<product_id>/', views.wish_list, name='wish_list'),
]
