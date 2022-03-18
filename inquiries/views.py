from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Inquiry

def inquiry(request):
    if request.method=="POST":
        name =request.POST.get('name',False) #False or 0
        place_name =request.POST.get('place_name',False)
        agent_id= request.POST.get('agent_id',False)
        email =request.POST.get('email',False)
        phone =request.POST.get('phone',False)
        message =request.POST.get('message')
        place_id =request.POST.get('place_id',False)

        if (name and place_name and email and phone and place_id and agent_id):
            check = Inquiry.objects.all().filter(name=name,property_name=place_name)
            if check:
                return redirect('/properties/'+place_id)
            else:
                user_inquiry=Inquiry(agent_id=agent_id, name=name,property_name=place_name,email=email,phone=phone,message=message)
                user_inquiry.save()
                if request.user.is_authenticated:
                    return redirect('dashboard')
                return redirect('/properties/'+place_id)
    return redirect('index')
