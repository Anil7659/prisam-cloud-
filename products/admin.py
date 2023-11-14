from django.contrib import admin

# Register your models here.
from . models import products 

class productadmin(admin.ModelAdmin):
    lis_disply = ()

admin.site.register(products, productadmin)