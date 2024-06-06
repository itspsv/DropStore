from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
# from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('edge_home', views.edge_home, name='edge_home'),
    # path('u_data', views.u_data, name='u_data'),
    # path('view_data', views.view_data, name='view_data'),
    # path('drop_let', views.drop_let, name='drop_let'),
    # path('profile', views.profile, name='profile'),
    # #lap
    # path('lap_edge_home', views.lap_edge_home, name='lap_edge_home'),
    # path('lap_u_data', views.lap_u_data, name='lap_u_data'),
    # path('lap_view_data', views.lap_view_data, name='lap_view_data'),
    # path('lap_drop_let', views.lap_drop_let, name='lap_drop_let'),
    # path('lap_u_profile', views.lap_u_profile, name='lap_u_profile'), 
    #ip cam
    path('cam_edge_home', views.cam_edge_home, name='cam_edge_home'),
    path('cam_u_data', views.cam_u_data, name='cam_u_data'),
    path('cam_view_data', views.cam_view_data, name='cam_view_data'),
    path('cam_drop_let', views.cam_drop_let, name='cam_drop_let'),
    path('cam-u-profile', views.cam_u_profile, name='cam_u_profile'),
    path('register-device', views.register_device, name='register_device'),
    path('view-files/<int:device_id>/<str:device_name>', views.view_files, name='view_files'),
    path('file-delete/<int:file_id>/<int:device_id>/<str:device_name>', views.file_delete, name='file_delete'),
    path('device-delete/<int:device_id>', views.device_delete, name='device_delete'),
    path('edge-backup', views.edge_backup, name='edge_backup'),
    
    
    
    # tab
    # path('tab_edge_home', views.tab_edge_home, name='tab_edge_home'),
    # path('tab_u_data', views.tab_u_data, name='tab_u_data'),
    # path('tab_view_data', views.tab_view_data, name='tab_view_data'),
    # path('tab_drop_let', views.tab_drop_let, name='tab_drop_let'),
    # path('tab_u_profile', views.tab_u_profile, name='tab_u_profile'),
]