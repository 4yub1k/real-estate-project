from django.shortcuts import render
from django.contrib.auth import logout
from .register_user  import reg_user
from inquiries.models import Inquiry
from django.contrib.auth.decorators import login_required

@login_required(login_url='/dashboard/signin/') 
def dashboard(request):
    inquiries=Inquiry.objects.filter(name=request.user.username)
    context = {
    'inquiries': inquiries
    }
    return render(request,'dashboard/dashboard.html',context)


def register(request):
    if request.method == "POST":
        user = reg_user(request) 
        return user
    else:
        return render(request,'dashboard/registration.html')
