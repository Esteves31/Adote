from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_pets, name="list_pets"),
    path('pedido_adocao/<int:id_pet>', views.adoption_application, name="adoption_application"),
]