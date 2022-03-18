from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def reg_user(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username exists !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email exists !')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,
                    last_name=last_name)
                    user.save()
                    #login after register use this --> 
                    auth.login(request, user)
                    return redirect('dashboard')
        else:
            #messages.error(request,'Passwords doesn\'t match')
            return redirect('register')
    else:
        return render(request,'dashboard/register.html')

