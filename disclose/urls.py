from django.urls import path
from . import views

urlpatterns = [
    path('novo_pet/', views.new_pet, name="new_pet"),
    path('seus_pets/', views.your_pets, name="your_pets"),
    path('remover_pet/<int:id>', views.remove_pet, name="remove_pet"),
    path('ver_pet/<int:id>', views.see_pet, name="see_pet"),
    path('ver_pedido_adocao/', views.see_adopt_application, name="see_adopt_application"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('api_adocoes_por_raca/', views.adoption_by_breed_api, name="adoption_by_breed_api"),
]