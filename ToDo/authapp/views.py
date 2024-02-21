from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def user_register(request):
    if request.method=='POST':
        un=request.POST['uname']
        up=request.POST['upass']
        ucp=request.POST['ucpass']
        uemail=request.POST['uemail']
        context={}
        if un=="" or up=="" or ucp=="" or uemail=="":
            context['errmsg']="Fields Cannot be Blank"
            return render(request,'authapp/register.html',context)
        elif up!=ucp:
            context['errmsg']="Password Didn't Match"
            return render(request,'authapp/register.html',context)
        else:
            u=User.objects.create(username=un,email=uemail)
            u.set_password(up)
            u.save()
            context['success']="Account created Successfully"
            return render(request,'authapp/register.html',context)
    else:
        return render(request,'authapp/register.html')
    
def user_login(request):
    if request.method=='POST':
        un=request.POST['uname']
        up=request.POST['upass']
        u=authenticate(username=un,password=up)
        if u is not None:
            login(request,u)
            return redirect('/home')
        else:
            context={}
            context['errmsg']='Invalid Username and Password'
            return render(request,'authapp/login.html',context)
    else:
        return render(request,'authapp/login.html')


def user_logout(request):
    logout(request)
    return redirect('/authapp/login')       