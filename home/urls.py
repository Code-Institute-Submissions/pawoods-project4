from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_update/', views.add_update, name='add_update'),
    path('edit_update/<int:update_id>/', views.edit_update, name='edit_update'),
    path('delete_update/<int:update_id>/', views.delete_update, name='delete_update'),
]
