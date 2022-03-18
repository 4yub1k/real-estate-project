from django.contrib import admin
from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name','property_name', 'email', 'phone','date_inquiry')
  list_display_links = ('id', 'name')
  list_filter = ('name',)
  search_fields = ('name','propoerty_name', 'email', 'phone','message')
  list_per_page = 25

admin.site.register(Inquiry, InquiryAdmin)
