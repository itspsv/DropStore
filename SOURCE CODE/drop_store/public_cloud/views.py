from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import *
from edge_node.models import *

# Create your views here.


def public_cloud_index(request):
    p=DeviceModel.objects.filter(device_status="pending").count()
    a=DeviceModel.objects.filter(device_status="accepted").count()
    d=DeviceModel.objects.all().count()
    f=FileModel.objects.all().count()
    return render(request, './public_cloud/public-cloud-index.html',{'p':p,'a':a,'d':d,'f':f,})

def public_edge_devices(request):
    d=DeviceModel.objects.filter(device_status='pending')
    return render(request, './public_cloud/public-edge-devices.html',{'d':d})

def public_droplet_fog_layer(request):
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
    return render(request, './public_cloud/public-droplet-fog-layer.html',{'d':d,})

def view_droplet_fog_layer(request,device_id):
    s=0
    f=FileModel.objects.filter(file_device=device_id).order_by('file_id')
    for i in f:
        s=i.file_size/1000000
        i.files_size = round(s,3)
    d=DeviceModel.objects.get(device_id=device_id)
    return render(request, './public_cloud/view-droplet-fog-layer.html',{'f':f,'d':d,'device_id':device_id})    
    

def accept_device(request,device_id):
    accept = get_object_or_404(DeviceModel,device_id=device_id)
    accept.device_status = "accepted"
    accept.save(update_fields=["device_status"]) 
    accept.save()
    if accept:
        messages.success(request,"Succesflly Accepted")

    return redirect('public_edge_devices')

def decline_device(request,device_id):
    decline = get_object_or_404(DeviceModel,device_id=device_id)
    decline.device_status = "declined"
    decline.save(update_fields=["device_status"])
    decline.save()
    if decline:
        messages.info(request,"Succesflly Rejected")
    return redirect('public_edge_devices')
    
def data_delete(request,file_id,device_id):
    
    data = FileModel.objects.filter( file_id =file_id)
    
    data.delete()
    if data:
        messages.success(request,"File Deleted Successfully")
        # return redirect('view_fog_layer')
    else:
        messages.success(request,"File Deleted Successfully")
        # return redirect('view_fog_layer')
    return redirect('view_droplet_fog_layer', device_id=device_id)