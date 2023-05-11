from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_agents, name='agents'),
    path('<int:pk>/', views.show_detail_agents, name='current_agent'),
    path('create/profile/', views.create_agent, name='create_profile'),
    path('create/user/', views.create_user, name='create_user'),
    path('create/org/', views.create_org, name='create_org'),
    path('create/address/', views.create_address, name='create_address'),
    path('<int:pk>/update/profile/', views.update_agent, name='update_profile'),
    path('<int:pk>/update/user/', views.update_user, name='update_user'),
    path('<int:pk>/update/org/', views.update_org, name='update_org'),
    path('<int:pk>/update/address/', views.update_address,
         name='update_address'),
    path('<int:pk>/delete/', views.delete_profile, name='delete_profile'),
]
