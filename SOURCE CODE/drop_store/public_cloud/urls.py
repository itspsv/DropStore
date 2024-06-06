from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('public-cloud-index', views.public_cloud_index, name='public_cloud_index'),
    path('public-edge-devices', views.public_edge_devices, name='public_edge_devices'),
    path('public-droplet-fog-layer', views.public_droplet_fog_layer, name='public_droplet_fog_layer'),
    path('view-droplet-fog-layer/<int:device_id>', views.view_droplet_fog_layer, name='view_droplet_fog_layer'),
    path('accept-device/<int:device_id>', views.accept_device, name='accept_device'),
    path('decline-device/<int:device_id>', views.decline_device, name='decline_device'),
    path('data-delete/<int:file_id>/<int:device_id>', views.data_delete, name='data_delete'),

    
]