from django.shortcuts import render
from listings.models import Listing
from listings.choices import bedroom_number,price_range,state_name
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def property_id(request, property_id):
    listings=Listing.objects.get(pk=property_id)
    context = {
        'listing':listings,
    }
    return render(request,'listings/listing.html',context)

def property_search(request):
    search=Listing.objects.order_by("-list_date")
    
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            search=search.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET.get('city')
        if city:
            search=search.filter(city__iexact=city) 

    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            search=search.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        if bedrooms:
            search=search.filter(bedrooms=bedrooms)

    if 'price' in request.GET:
        price = request.GET.get('price')
        if price:
            search=search.filter(price__lte=price)
    """Paginator"""
    paginator=Paginator(search,3)

    page_number = request.GET.get('page')
    page_property = paginator.get_page(page_number)
    context = {
        'listings':page_property,
        'bedroom_number':bedroom_number,
        'price_range':price_range,
        'state_name':state_name
    }
    return render(request,'listings/listings.html',context)

def properties(request):
    page_property=Listing.objects.order_by("-list_date")
    paginator=Paginator(page_property,3) #show 3 only

    page_number = request.GET.get('page')
    page_property = paginator.get_page(page_number)
    context = {
        'listings':page_property,
        'bedroom_number':bedroom_number,
        'price_range':price_range,
        'state_name':state_name
    }
    return render(request,'listings/listings.html',context)