from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'price', 'created_at', 'auction']

admin.site.register(Advertisements, AdvertisementAdmin)

# Register your models here.
