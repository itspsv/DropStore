from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import *
from drop_store.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives

def home(request):
    
    return render(request, './main/index.html')



def edge_login(request):
    if request.method == "POST":
        username=request.POST.get("email")
        password=request.POST.get("password")
        print(username,password)

        try:
            # s1=UserModel.objects.filter(user_status="accepted") | UserModel.objects.filter(user_status="warned")
            auth = UserdetailsModel.objects.get(user_email=username,user_password=password)
            if auth.user_status  == "accepted":
                request.session['user_id'] = auth.user_id
                messages.success(request,'Successfully Logged In')
                return redirect('cam_edge_home')
            elif auth.user_status == "pending":
                messages.info(request,'Your id is pending for registration ')
                return redirect('droplet_login')
            elif auth.user_status == "blocked":
                messages.error(request,'You Are BLOCKED From Logging In ')
                return redirect('droplet_login')
            else:
                messages.error(request,'You are not registered,try again after signup')
                return redirect('droplet_login')
            
        except:
            messages.error(request,'invalid login credentials')
            return redirect('droplet_login')

    return render (request, "./main/edge-login.html")

def droplet_login(request):
    if request.method == "POST":
        username=request.POST.get("email")
        password=request.POST.get("password")
        

        if username == "droplet" and password == "droplet":
            messages.success(request,'Successfully Login')
            return redirect('droplet_index')
        else:
            messages.error(request,'invalid login credentials')
            return redirect('droplet_login')

        # try:
        #     # s1=UserModel.objects.filter(user_status="accepted") | UserModel.objects.filter(user_status="warned")
        #     auth = UserdetailsModel.objects.get(user_email=username,user_password=password)
        #     if auth.user_status  == "accepted":
        #         request.session['user_id'] = auth.user_id
        #         messages.success(request,'Successfully Logged In')
        #         return redirect('cam_edge_home')
        #     elif auth.user_status == "pending":
        #         messages.info(request,'Your id is pending for registration ')
        #         return redirect('droplet_login')
        #     elif auth.user_status == "blocked":
        #         messages.error(request,'You Are BLOCKED From Logging In ')
        #         return redirect('droplet_login')
        #     else:
        #         messages.error(request,'You are not registered,try again after signup')
        #         return redirect('droplet_login')
            
        # except:
        #     messages.error(request,'invalid login credentials')
        #     return redirect('droplet_login')

    return render (request, "./main/droplet-login.html")

def dropstore_login(request):
    if request.method == "POST":
        username=request.POST.get("email")
        password=request.POST.get("password")
        print(username,password)

        if username == "dropstore" and password == "dropstore":
            messages.success(request,'Successfully Login')
            return redirect('dropstore_index')
        else:
            messages.error(request,'invalid login credentials')
            return redirect('dropstore_login')
    return render (request, "./main/dropstore-login.html")

def public_login(request):
    if request.method == "POST":
        username=request.POST.get("email")
        password=request.POST.get("password")
        print(username,password)

        if username == "public" and password == "public":
            messages.success(request,'Successfully Login')
            return redirect('public_cloud_index')
        else:
            messages.error(request,'invalid login credentials')
            return redirect('public_login')
    return render (request, "./main/public-login.html")

def user_reg(request):
    if request.method == "POST" and request.FILES["file"] :
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['pass']
        select = request.POST['select']
        image = request.FILES['file']
        

        try:
            s=UserdetailsModel.objects.get(user_email=email)
            messages.info(request,"Email already exists,try again with another email")
        except:

        
            s1=UserdetailsModel.objects.create(user_name=name,user_email=email,user_password=password,user_contact=phone,user_region=select,user_photo=image)
            s1.save()
            
            if s1:
                messages.success(request,"successfully Registered")
                return redirect('user_reg')
            else:
                messages.error(request,"invalid details ,try again")
                return redirect('user_reg')

    return render (request, './main/user-register.html')

# def l_reg(request):
#     if request.method == "POST" and request.FILES["file"] :
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         password = request.POST['pass']
#         image = request.FILES['file']
#         reg_details = lap_reg.objects.create(name=name,phone=phone,email=email,pwd=password,image=image)
#         reg_details.save()
#     return render (request, './main/lap-reg.html')

# def cam_reg (request):
#     if request.method == "POST" and request.FILES["file"] :
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         password = request.POST['pass']
#         image = request.FILES['file']
#         reg_details = camera_reg.objects.create(name=name,phone=phone,email=email,pwd=password,image=image)
#         reg_details.save()
#     return render (request, './main/cam-reg.html')



# def t_reg (request):
#     if request.method == "POST" and request.FILES["file"] :
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         password = request.POST['pass']
#         image = request.FILES['file']
#         reg_details = tab_reg.objects.create(name=name,phone=phone,email=email,pwd=password,image=image)
#         reg_details.save()
#     return render (request, './main/tab-reg.html')


# def m_login (request):
#     return render (request, './main/login.html')

# def l_login (request):
#     return render (request, './main/l-login.html')

# def t_login (request):
#     return render (request, './main/t-login.html')

# def ip_login (request):
#     return render (request, './main/ip-login.html')