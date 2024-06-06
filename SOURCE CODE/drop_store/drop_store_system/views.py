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



def dropstore_index(request):
    # p=UserdetailsModel.objects.filter(user_status="pending").count()
    a=UserdetailsModel.objects.all().count()
    b=DeviceModel.objects.all().count()
    c=FileModel.objects.all().count()
    return render(request, './dropstore/dropstore-index.html',{'a':a,'b':b,'c':c,})

def dropstore_edge_nodes(request):
    d=DeviceModel.objects.all()
    print(d,'fvsddvdvv')
    
    global c,c2,c3
    c=0
    c2=0
    c3=0

    for i in d:
        c=0
        files_size=FileModel.objects.filter(file_node="Asia")
        for j in files_size:
        # print(files_size,'asdasd')
            a = j.file_size
            
            c+=a/1000000
            c= round(c,3)
    for i in d:
        c2=0
        files_size=FileModel.objects.filter(file_node="North America")
        for j in files_size:
        # print(files_size,'asdasd')
            a = j.file_size
            
            c2+=a/1000000
            c2= round(c2,3)

    for i in d:
        c3=0
        files_size=FileModel.objects.filter(file_node="Europe")
        for j in files_size:
        # print(files_size,'asdasd')
            a = j.file_size
            
            c3+=a/1000000
            c3 = round(c3,3)
    return render(request, './dropstore/dropstore-edge-nodes.html',{'a':c,'b':c2,'c':c3})
# ,{'a':i.file_size1,'b':i.file_size2,'c':i.file_size3}

def dropstore_droplet_fog_layer(request):
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
    return render(request, './dropstore/dropstore-droplet-fog-layer.html',{'d':d})

    

def s_view_droplet_fog_layer(request,device_id):
    s=0
    f=FileModel.objects.filter(file_device=device_id).order_by('file_id')
    for i in f:
        s=i.file_size/1000000
        i.files_size = round(s,3)
    d=DeviceModel.objects.get(device_id=device_id)
    return render(request, './dropstore/s-view-droplet-fog-layer.html',{'f':f,'d':d,'device_id':device_id})

def data_delete(request,file_id,device_id):
    
    data = FileModel.objects.filter( file_id =file_id)
    
    data.delete()
    if data:
        messages.success(request,"File Deleted Successfully")
        # return redirect('view_fog_layer')
    else:
        messages.success(request,"File Deleted Successfully")
        # return redirect('view_fog_layer')
    return redirect('s_view_droplet_fog_layer', device_id=device_id)