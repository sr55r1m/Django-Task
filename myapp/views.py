from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.forms import RegisterForm
from myapp.models import Register
from django.core.mail import send_mail
from validations import settings
import random
# Create your views here.

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            username=request.POST['first_name']+"@apssdc.in"
            pwd=random.randint(1000,9999)
            form.save()
            data=Register.objects.get(email=request.POST['email'])
            data.password=pwd
            data.username=username
            data.save()
            send_mail("Your Data Registered Succesfully","Your Username: " +email+ "Your Password is: "+str(pwd),settings.EMAIL_HOST_USER,[email])
            return HttpResponse("Check Your Mail")

        return HttpResponse("Already Registered")
    form=RegisterForm()
    return render(request,'myapp/register.html',{'form':form})

def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upassword=request.POST['upassword']
        data=Register.objects.get(username=uname,password=upassword)
        if data:
            return redirect('/cpassword')
    return render(request,'myapp/login.html')

def cpassword(request):
    if request.method=="POST":
        op=request.POST['oldpassword']
        np=request.POST['newpassword']
        cp=request.POST['confirmpassword']
        data=Register.objects.get(password=op)
        if np!=cp:
            return HttpResponse("Wrong Password Details")
        else:
            data.password=cp
            data.save()
            return HttpResponse("Welcome")
    return render(request,'myapp/change.html')
