from django.contrib import admin
from .models import Banner
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
  list_display = ('id', 'title','description')
  list_display_links = ('id', 'title')
  list_filter = ('title',)
  search_fields = ('title', 'description',)
  list_per_page = 25

admin.site.register(Banner, BannerAdmin)