from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title','state', 'is_published', 'price', 'list_date', 'agent')
  list_display_links = ('id', 'title')
  list_filter = ('agent',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)