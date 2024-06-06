from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import *
import pathlib 
import socket
from drop_store.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives


def cam_edge_home(request):
    return render(request, './edge-node/user/edge-home.html')

def cam_u_data(request):
    auth=request.session['user_id']
    user=UserdetailsModel.objects.get(user_id=auth)
    r=user.user_region
    d1=DeviceModel.objects.filter(device_user=user,device_status="accepted")
    d2=DeviceModel.objects.filter(device_user=user).values('device_type')
    print(d1)
    # d3=DeviceModel.objects.get(device_id=id)
    # d4=user.file_device.all()
    # global ax
    # ax=''
    # for a in d1:
    #    ax += a.device_type
    
    # print(ax,'asdasdasad')

    
    global c1
    c1=None
    if request.method == "POST" and request.FILES["file1"] :
        file = request.FILES['file1']
        f_name=file.name
        f_size = file.size
        f_type = pathlib.Path(f'{f_name}').suffix
        device_id = request.POST['device']
        device = DeviceModel.objects.get(pk=device_id)
        # if device in d2.device_type:
        #     d=DeviceModel.objects.get(device_user=user,device_type=device)
        #     c1 +=d.device_id
        #     print(c1,'asdasdasdasd')
        # else:
        #     print('fdsdsdfsdf')
        # c=c1
        u_details = FileModel.objects.create(file_name=f_name,file_size=f_size,file_type=f_type, file=file,file_user=user,file_device=device,file_node=r)
        u_details.save()
        if u_details:
            messages.success(request,"Succesflly Uploaded")
            return redirect("cam_u_data")

        else:
            messages.error(request,"No changes detected")
            return redirect("cam_u_data")
    return render (request, './edge-node/user/upload-data.html',{'d':d1})
 
def cam_view_data(request):
    auth=request.session['user_id']
    user=UserdetailsModel.objects.get(user_id=auth)
    d1=DeviceModel.objects.filter(device_user=user.user_id)
    for i in d1:
        files_count=FileModel.objects.filter(file_device=i.device_id).count()
        i.file_count = files_count
    global c
    c=0
    for i in d1:
        files_count=FileModel.objects.filter(file_device=i.device_id).count()
        i.file_count = files_count
    for i in d1:
        c=0
        files_size=FileModel.objects.filter(file_device=i.device_id)
        for j in files_size:
        # print(files_size,'asdasd')
            a = j.file_size
            
            c+=a/1000000
            i.file_size = round(c,3)
    # c1=FileModel.objects.filter(file_device=)
    print(c,'asdfascv')

    return render (request, './edge-node/user/view-data.html',{'v':d1})

def cam_drop_let(request):
    return render (request, './edge-node/user/drop-let.html')

def cam_u_profile(request):
    user_id=request.session['user_id']
    user=UserdetailsModel.objects.get(user_id=user_id)
    device=DeviceModel.objects.filter(device_user=user_id).count()

    
    if request.method=="POST":
        if len(request.FILES) ==0:
            name=request.POST.get("name")
            
            email=request.POST.get("email")
            password=request.POST.get("password")
            contact=request.POST.get("contact")
            
            # photo=request.FILES["photo"]
            user.user_name = name
            
            user.user_email = email
            user.user_password = password
            user.user_contact = contact
        
        # user.user_country = country

            user.save()
            if user:
                messages.success(request,"Succesflly Updated")
                

            else:
                messages.error(request,"No changes detected")
                return redirect("cam_u_profile")
        else:
            if request.method=="POST" and request.FILES['file1']:
                profile=request.FILES['file1']
                name=request.POST.get("name")
                
                email=request.POST.get("email")
                password=request.POST.get("password")
                contact=request.POST.get("contact")
                
                # photo=request.FILES["photo"]
                user.user_name = name
                user.user_photo = profile
                user.user_email = email
                user.user_password = password
                user.user_contact = contact
                
                # user.user_country = country

                user.save()
                if user:
                    messages.success(request,"Succesflly Updated")
                
                

                    

                else:
                    messages.error(request,"No changes detected")
                    return redirect("cam_u_profile")


    return render (request, 'edge-node/user/cam-u-profile.html',{'a':user,'b':device})
    

def view_files(request,device_id,device_name):
    data=FileModel.objects.filter(file_device=device_id)
    data1= device_name
    global c
    c=0
    for i in data:
        c=0
        # files_size=FileModel.objects.get(file_device=i.file_device)
        
        # print(files_size,'asdasd')
        a = i.file_size
        
        c+=a/1000000
        i.file_sizes = round(c,3)

    return render (request, 'edge-node/user/view-files.html',{'a':data,'b':data1,'device_id':device_id,'device_name':device_name})

def register_device(request):
    user_id=request.session['user_id']
    user=UserdetailsModel.objects.get(user_id=user_id)
    r=user.user_region
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(IPAddr)
    user.ip_address = IPAddr
    if request.method == "POST":
        type=request.POST.get("type")
        name=request.POST.get("name")
        ip=request.POST.get("ip")
        server=request.POST.get("server")
        print(type,name,ip,'first line')

        try:
            
            d1=DeviceModel.objects.get(device_ip=ip)
            
            messages.error(request,"Device already exists,try again with another device")
            return redirect('register_device')
        except:
            print('except error')

        
            d=DeviceModel.objects.create(device_type=type,device_name=name,device_ip=ip,device_user=user,device_node=server)
            d.save()
            if d:
                messages.success(request,"successfully Registered")
                
            else:
                messages.error(request,"invalid details ,try again")
                return redirect('register_device')
    return render (request, 'edge-node/user/register-device.html',{'user':user})


def edge_backup(request):
    user_id=request.session['user_id']
    user=UserdetailsModel.objects.get(user_id=user_id)
    if request.method == "POST":
        server=request.POST.get("server")
        password=request.POST.get("password")
        if user.user_password == password:
            backup = get_object_or_404(UserdetailsModel,user_id=user_id)
            backup.user_server = server
            backup.save(update_fields=["user_server"])
            backup.save()
            device_backup = DeviceModel.objects.filter(device_user=user_id)
            print(device_backup,'asdasdasdasdasdadasd')
            

            html_content = "<p>Dear User,</p><br><p>Your request for one touch backup is Successful, In case of any data loss you can retrive your data from the following :</p><span><strong>" + \
                server + "</strong></span>"
            from_mail = DEFAULT_FROM_EMAIL

            to_mail = [user.user_email]
            print(html_content,from_mail,to_mail,'asdasdasdasdsdd')
            msg = EmailMultiAlternatives(
                "Backup Successful", html_content, from_mail, to_mail)
            msg.attach_alternative(html_content, "text/html")
            print(html_content,from_mail,to_mail,msg,'asdasdasdasdsdd')
            msg.send()

            for i in device_backup:
                i.device_server = server
                print(i.device_server,'vvvvvvvvvv')
                
                i.save()
            if backup and i.device_server:
                messages.success(request,"Data Backedup Successfully")
                return redirect('edge_backup')
        
    return render(request,'edge-node/user/edge-backup.html')

def file_delete(request,file_id,device_id,device_name):
    
    msg = FileModel.objects.filter( file_id =file_id)
    
    msg.delete()
    if msg:
        messages.success(request,"File Deleted Successfully")
    else:
        messages.success(request,"File Deleted Successfully")
        # return redirect('view_files')
    return redirect('view_files',device_id=device_id,device_name=device_name)

def device_delete(request,device_id):
    
    msg = DeviceModel.objects.filter( device_id =device_id)
    
    msg.delete()
    if msg:
        messages.success(request,"Device Deleted Successfully")
    else:
        messages.success(request,"Device Deleted Successfully")
        return redirect('cam_view_data')
    return render(request,'edge-node/user/view-data.html')








# def edge_home(request):
#     return render(request, './edge-node/mobile/edge-home.html')

# def u_data(request):
#     if request.method == "POST" and request.FILES["file1"] :
#         f_name = request.POST['file1']
#         f_size = request.POST['size']
#         f_type = pathlib.Path(f'{f_name}').suffix
#         u_details = upload_data.objects.create(file_name=f_name,file_size=f_size,file_type=f_type, file=file)
#         u_details.save()
#     return render (request, './edge-node/mobile/upload-data.html')

# def view_data(request):
#     return render (request, './edge-node/mobile/view-data.html')

# def drop_let(request):
#     return render (request, './edge-node/mobile/drop-let.html')

# def profile (request):
#     return render (request, './edge-node/mobile/my-profile.html')


# laptop-data 

# def lap_edge_home(request):
#     return render(request, './edge-node/lap/edge-home.html')

# def lap_u_data(request):
#     if request.method == "POST" and request.FILES["file1"] :
#         f_name = request.POST['file1']
#         f_size = request.POST['size']
#         f_type = pathlib.Path(f'{f_name}').suffix
#         u_details = lap_data.objects.create(file_name=f_name,file_size=f_size,file_type=f_type, file=file)
#         u_details.save()
#     return render (request, './edge-node/lap/upload-data.html')

# def lap_view_data(request):
#     return render (request, './edge-node/lap/view-data.html')

# def lap_drop_let(request):
#     return render (request, './edge-node/lap/drop-let.html')

# def lap_u_profile (request):
#     return render (request, './edge-node/lap/my-profile.html')

#ip camera




#  tab

# def tab_edge_home(request):
#     return render(request, './edge-node/tab/edge-home.html')

# def tab_u_data(request):
#     if request.method == "POST" and request.FILES["file1"] :
#         f_name = request.POST['file1']
#         f_size = request.POST['size']
#         f_type = pathlib.Path(f'{f_name}').suffix
#         u_details = tab_data.objects.create(file_name=f_name,file_size=f_size,file_type=f_type, file=file)
#         u_details.save()
#     return render (request, './edge-node/tab/upload-data.html')

# def tab_view_data(request):
#     return render (request, './edge-node/tab/view-data.html')

# def tab_drop_let(request):
#     return render (request, './edge-node/tab/drop-let.html')

# def tab_u_profile (request):
#     return render (request, './edge-node/tab/my-profile.html')



