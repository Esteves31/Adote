from django.urls import path
from . import views

urlpatterns = [
    path('novo_pet/', views.new_pet, name="new_pet"),
]