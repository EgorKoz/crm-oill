from django.urls import path
from . import views

urlpatterns = [
    path('', views.appeal, name='appeal'),
    path('<int:pk>/', views.appeal_current, name='appeal_current'),
    path('create/', views.appeal_create, name='appeal_create'),
    path('<int:pk>/update/', views.appeal_update, name='appeal_update'),
    path('<int:pk>/delete/', views.delete_appeal, name='appeal_delete'),
]
