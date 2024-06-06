from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
    path('droplet-fog-layer', views.droplet_fog_layer, name='droplet_fog_layer'),
    path('droplet-index', views.droplet_index, name='droplet_index'),
    path('droplet-pending', views.droplet_pending, name='droplet_pending'),
    path('view-fog-layer/<int:device_id>', views.view_fog_layer, name='view_fog_layer'),
    path('accept-user/<int:user_id>', views.accept_user, name='accept_user'),
    path('decline-user/<int:user_id>', views.decline_user, name='decline_user'),
    path('data-deleted/<int:file_id>/<int:device_id>', views.data_deleted, name='data_deleted'),

]

