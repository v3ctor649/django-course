from django.contrib import admin

from Site.models import Categories,Clothes,Profile,Orders,Order   #Profile_Cart
from django.utils.safestring import mark_safe
import os
# Register your models here.

class ClothesInline(admin.TabularInline):
    model = Clothes
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="/static/img/{obj.photo}" style="max-height: 200px;">')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="/static/img/{obj.photo}" style="max-height: 200px;">')

    list_display = ['name']
    inlines = [
       ClothesInline
    ]


class Profile_Order_Inline(admin.TabularInline):
    model = Order

@admin.register(Orders)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','status','data_field','order_price']
    list_filter = ('status',)
    list_editable = ['status',]
    inlines = [
       Profile_Order_Inline
    ]











