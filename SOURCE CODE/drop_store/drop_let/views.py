from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import *
from mainapp.models import UserdetailsModel
from edge_node.models import DeviceModel
from edge_node.models import FileModel

import socket


# Create your views here.

# def droplet_login(request):
#     return render(request, './main/droplet-login.html')

def droplet_index(request):
    p=UserdetailsModel.objects.filter(user_status="pending").count()
    a=UserdetailsModel.objects.filter(user_status="accepted").count()
    d=DeviceModel.objects.all().count()
    f=FileModel.objects.all().count()
    return render(request, './drop_let/droplet-index.html',{'p':p,'a':a,'d':d,'f':f,})

def droplet_pending(request):
    p=UserdetailsModel.objects.filter(user_status="pending")
    return render(request, './drop_let/droplet-pending.html',{'p':p})

def droplet_fog_layer(request):
    d=DeviceModel.objects.all()
    print(d,'fvsddvdvv')
    
    global c
    c=0
    for i in d:
        files_count=FileModel.objects.filter(file_device=i.device_id).count()
        i.file_count = files_count
    for i in d:
        c=0
        files_size=FileModel.objects.filter(file_device=i.device_id)
        for j in files_size:
        # print(files_size,'asdasd')
            a = j.file_size
            
            c+=a/1000000
            i.file_size = round(c,3)
        # print(i.file_size,'vvvvvv')
    # for h in d:
    #     print(h.file_count,'gdfdgfdgdfdg')
  
   
    return render(request, './drop_let/droplet-fog-layer.html',{'d':d,})

def view_fog_layer(request,device_id):
    s=0
    f=FileModel.objects.filter(file_device=device_id).order_by('file_id')
    for i in f:
        s=i.file_size/1000000
        i.files_size = round(s,3)
    d=DeviceModel.objects.get(device_id=device_id)
    return render(request, './drop_let/view-fog-layer.html',{'f':f,'d':d,'device_id':device_id})

def accept_user(request,user_id):
    accept = get_object_or_404(UserdetailsModel,user_id=user_id)
    accept.user_status = "accepted"
    accept.save(update_fields=["user_status"])
    accept.save()
    if accept:
        messages.success(request,"User Added Successfully")

    return redirect('droplet_pending')

def decline_user(request,user_id):
    decline = get_object_or_404(UserdetailsModel,user_id=user_id)
    decline.user_status = "declined"
    decline.save(update_fields=["user_status"])
    decline.save()
    if decline:
        messages.success(request,"Rejected Successfully")

    return redirect('droplet_pending')

def data_deleted(request,file_id,device_id):
    
    data = FileModel.objects.filter( file_id =file_id)
    
    data.delete()
    if data:
        messages.success(request,"File Deleted Successfully")
        return redirect('view_fog_layer')
    else:
        messages.success(request,"File Deleted Successfully")
        # return redirect('view_fog_layer')
    return redirect('view_fog_layer', device_id=device_id)

