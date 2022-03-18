from django.urls import path
from . import views
urlpatterns = [
    path('',views.properties,name='properties'),
    path('<int:property_id>/',views.property_id,name='property_id'),
    path('search/',views.property_search,name='property_search'),
]
