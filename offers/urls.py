from django.urls import path
from . import views

urlpatterns = [
    path('', views.offers, name='offers'),
    path('<int:pk>/', views.offer_current, name='offer_current'),
    path('create/', views.create_offer, name='offer_create'),
]