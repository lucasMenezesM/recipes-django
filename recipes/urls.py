from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('about/', views.about)
]
