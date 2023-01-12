from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.signup, name="signup"),
    path('login/', views.signin, name="signin"),
    path('sair/', views.log_out, name="log_out"),
]