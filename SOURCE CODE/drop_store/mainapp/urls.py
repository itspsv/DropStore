from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 



urlpatterns = [
    path('', views.home, name='home'),
    path ('edge-login', views.edge_login, name = "edge_login"),
    # path ('edge_login', views.edge_login, name = "edge_login"),
    path ('user-register', views.user_reg, name = "user_reg"),
    # path ('lap-reg', views.l_reg, name = "l_reg"),
    # path ('cam-reg', views.cam_reg, name = "cam_reg"),
    # path ('tab-reg', views.t_reg, name = "t_reg"),
    # path ('m_login', views.m_login, name = "m_login"),
    # path ('ip_login', views.ip_login, name = "ip_login"),
    # path ('l_login', views.l_login, name = "l_login"),
    # path ('t_login', views.t_login, name = "t_login"),
    path ('droplet-login', views.droplet_login, name = "droplet_login"),
    path ('dropstore-login', views.dropstore_login, name = "dropstore_login"),
    path ('public-login', views.public_login, name = "public_login"),
]