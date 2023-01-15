from django.urls import path
from . import views

urlpatterns = [
    path('novo_pet/', views.new_pet, name="new_pet"),
    path('seus_pets/', views.your_pets, name="your_pets"),
    path('remover_pet/<int:id>', views.remove_pet, name="remove_pet"),
    path('ver_pet/<int:id>', views.see_pet, name="see_pet"),
]