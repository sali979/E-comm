from django.contrib import admin
from .models import Product
from .models import Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    #def change_category_to_default(self,request,queryset):
    #    queryset.update('title', 'price', 'discount_price', 'category', 'description', 'image')

    list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    search_fields = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    #actions = ('')

admin.site.register(Product)
admin.site.register(Order)