from django.shortcuts import render,redirect
from .models import User
from .helper import send_otp_api
import http.client
import random
from django.conf import settings
from django.core.cache import cache
# Create your views here.

def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('mobile')

        user = User.objects.filter(phone_number = phone_number).first()
        print(user)

        if user is None:
            context = { 'message': 'User not found','class':'danger'}
            return render(request,'login.html',context)

        otp = str(random.randint(1000,9999))
        print(otp)
        User.otp=otp
        user.save()
        send_otp_api(phone_number,otp)
        request.session['phone_number'] = phone_number
        return redirect('otp')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('mobile')
        password = request.POST.get('password')
        
        check_user = User.objects.filter(phone_number = phone_number).first()
        if check_user:
            context = {'message' : 'User already exists' , 'class' : 'danger' }
            return render(request,'register.html' , context)
        otp = str(random.randint(1000 , 9999))
        print(otp)
        User.otp=otp
        user = User.objects.create(phone_number = phone_number,name=name,password=password,otp=otp)
        user.save()
        send_otp_api(phone_number,otp)
        request.session['phone_number'] = phone_number
        return redirect('otp')
    return render(request,'register.html')

def otp(request):
    phone_number = request.session['phone_number']
    context = {'mobile':phone_number}
    if request.method == 'POST':
        otp = request.POST.get('otp')

        user = User.objects.filter(phone_number=phone_number).first()
        if otp == User.otp:
            return redirect('welcome')
        else:
            print("wrong otp")
            context = {'message' : 'Wrong OTP entered' , 'class' : 'danger' , 'mobile':phone_number}
            return render(request,'otp.html',context)   
    return render(request,'otp.html',context)


def welcome(request):
    user = User.objects.get(phone_number=request.session['phone_number'])
    name = user.name
    print(name)
    context = {'name': name }
    return render(request,'welcome.html',context)
