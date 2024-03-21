
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect
from Home.models import Contact
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User

user=None
def home(request):
    if request.user.is_authenticated:
        context={
            "hom":"active",
            "act":"",
            "about":"",
            "service":"",
            "contac":"",
            "log":"myaccount",
            "logtext":"My Account",
            "hid":"",
            "lok":"logout",
            "logtex":"Logout",      
        }
    else:
        context={
            "hom":"active",
            "about":"",
            "service":"",
            "contac":"",
            "log":"login",
            "logtext":"Login",
            "act":"",
            "lok":"",
            "hid":"hidden",
            "logtex":"",
            
        }
    return render(request,'index',context)

def about(request):
    if request.user.is_authenticated:
        context={
            "hom":"",
            "about":"active",
            "service":"",
            "contac":"",
            "hid":"",
            "act":"",
            "log":"myaccount",
            "logtext":"My Account",
            "lok":"logout",
            "logtex":"Logout",      
        }
    else:
        context={
            "hom":"",
            "about":"active",
            "act":"",
            "service":"",
            "contac":"",
            "hid":"hidden",
            "log":"login",
            "logtext":"Login",
            "lok":"",
            "logtex":"",
        }
    return render(request,'about',context)

def services(request):
    if request.user.is_authenticated:
        context={
            "hom":"",
            "about":"",
            "service":"active",
            "contac":"",
            "log":"myaccount",
            "act":"",
            "hid":"",
            "logtext":"My Account",
            "lok":"logout",
            "logtex":"Logout",      
        }
    else:
        context={
            "hom":"",
            "about":"",
            "service":"active",
            "act":"",
            "contac":"",
            "log":"login",
            "logtext":"Login",
            "lok":"",
            "hid":"hidden",
            "logtex":"",
            
        }
    
    return render(request, 'services',context)

def contact(request):
    if request.user.is_authenticated:
        context={
            "hom":"",
            "about":"",
            "service":"",
            "contac":"active",
            "act":"",
            "log":"myaccount",
            "hid":"",
            "logtext":"My Account",
            "lok":"logout",
            "logtex":"Logout",   
        }
    else:
        context={
            "hom":"",
            "about":"",
            "service":"",
            "act":"",
            "contac":"active",
            "log":"login",
            "logtext":"Login",
            "hid":"hidden",
            "lok":"",
            "logtex":"",
        }
    
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name, email=email, phone= phone, desc= desc, date= datetime.today())
        contact.save()
        messages.success(request, f'Your message has been sent,{name}!')
    return render(request,'contact',context)

def loginUser(request):
    global user
    if request.user.is_authenticated:
        context={
            "hom":"",
            "about":"",
            "service":"",
            "contac":"",
            "act":"active",
            "log":"myaccount",
            "logtext":"My Account",
            "lok":"logout",
            "hid":"",
            "logtex":"Logout",     
        }
    else:
        context={
            "hom":"",
            "about":"",
            "service":"",
            "act":"active",
            "contac":"",
            "log":"login",
            "hid":"hidden",
            "logtext":"Login",
            "lok":"",
            "logtex":"", 
        }
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/myaccount')
        
        else:
            messages.warning(request, 'Your password or username is incorrect!')
            
    return render(request,'login',context)

def signup(request):
    if request.user.is_authenticated:
        context={
            "hom":"",
            "about":"",
            "service":"",
            "contac":"",
            "act":"",
            "log":"myaccount",
            "logtext":"My Account",
            "lok":"logout",
            "hid":"",
            "logtex":"Logout",     
        }
    else:
        context={
            "hom":"",
            "about":"",
            "service":"",
            "act":"active",
            "contac":"",
            "hid":"hidden",
            "log":"login",
            "logtext":"Login",
            "lok":"",
            "logtex":"",
        }
    if request.method=="POST":
        name= request.POST.get('name')
        username= request.POST.get('username')
        email=request.POST.get('email')
        password= request.POST.get('password')
        try :
            user=User.objects.create_user(username,email,password)
            user.save()
            messages.success(request, f'Your account has been created,{username}!')
            return redirect('/login')
        except :
            messages.warning(request, f'Username is not available!')
            
            
            
        
        
    return render(request,'signup',context)

def myaccount(request): 
    if request.user.is_authenticated:
        context={
            "hom":"",
            "about":"",
            "service":"",
            "act":"active",
            "contac":"",
            "log":"myaccount",
            "hid":"",
            "logtext":"My Account",
            "lok":"logout",
            "logtex":"Logout", 
                
        }
    else:
        context={
        }
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request,'myaccount',context)

def logoutUser(request):
    
    if request.user.is_authenticated:
        logout(request)
    return redirect("/login")