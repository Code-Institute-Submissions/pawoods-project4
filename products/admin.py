from django.contrib import admin
from .models import Product, Category, SubCategory, Brand


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'sub_category',
        'price',
        'image',
    )

    ordering = ('sku',)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'category',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
