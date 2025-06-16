from django.contrib import admin
from .models import Cart, CartItem

class cartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date_added')

class cartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart' , 'quantity' , 'is_active')


# Register your models here.
admin.site.register(Cart , cartAdmin)
admin.site.register(CartItem , cartItemAdmin)