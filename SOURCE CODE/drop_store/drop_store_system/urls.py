from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('dropstore-index', views.dropstore_index, name='dropstore_index'),
    path('dropstore-edge-nodes', views.dropstore_edge_nodes, name='dropstore_edge_nodes'),
    path('dropstore-droplet-fog-layer', views.dropstore_droplet_fog_layer, name='dropstore_droplet_fog_layer'),
    path('s-view-droplet-fog-layer/<int:device_id>', views.s_view_droplet_fog_layer, name='s_view_droplet_fog_layer'),
    path('data-delete/<int:file_id>/<int:device_id>', views.data_delete, name='data_delete'),
]