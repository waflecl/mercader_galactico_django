from django.urls import path
from mercader_galactico import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pregunta/', views.pregunta, name='pregunta'),
]