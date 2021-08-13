from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from Product import (templates,static)

# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('https://bedsdivan-62f7b.web.app/')
            else:
                return render(request,'login.html',{'error':True})
        else:
            return render(request,'login.html',{'error':True})
    else:
        return render(request,'login.html')