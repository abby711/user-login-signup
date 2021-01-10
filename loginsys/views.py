from django.shortcuts import render
from loginsys.models import newuser
from django.contrib import messages
def indexpage(request):
    return render(request,'index.html')

def registeruser(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        namee=request.POST['firstname']
        newuser(username=username,email=email,password=password,namee=namee).save()
        messages.success(request,'The new user '+request.POST['username']+'was registered successfully!')
        return render(request,'register.html')
    else:
        return render(request,'register.html')

def loginuser(request):
    if request.method=='POST':
        try:
            userdetails=newuser.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",userdetails)
            request.session["email"]=userdetails.email
            return render(request,'index.html')
        except newuser.DoesNotExist as e:
            messages.success(request,'Invalid details')

    else:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session["email"]
    except:
        return render(request,'index.html')
    return render(request,'index.html')
