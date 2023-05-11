from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='applications'),
    path('<int:pk>/', views.app_current, name='app_current'),
    path('create/', views.create_app_form, name='app_create'),
    path('<int:pk>/update/', views.update_app, name='app_update'),
    path('<int:pk>/send/', views.send_app, name='app_send'),
]
