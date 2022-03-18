from django.shortcuts import render
from listings.models import Listing
from blocks.models import Banner
from listings.choices import bedroom_number,price_range,state_name

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:4] #- for descending
    banners=Banner.objects.all()
    context = {
        'listings': listings,
        'banners': banners,
        'bedroom_number':bedroom_number,
        'price_range':price_range,
        'state_name':state_name
    }
    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')