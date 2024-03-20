from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number', 'date', 'total',
        'original_basket', 'stripe_pid',
    )

    fields = (
        'order_number', 'user_profile', 'date', 'first_name', 'last_name',
        'email', 'phone_number', 'postcode', 'country',
        'town_or_city', 'street_address_1', 'street_address_2',
        'county', 'total', 'original_basket', 'stripe_pid',
    )

    list_display = (
        'order_number',
        'date',
        'first_name',
        'last_name',
        'total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
