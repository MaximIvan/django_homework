from django.contrib import admin
from .models import Client, Product, Order
# Register your models here.


@admin.action(description="сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.action(description="товар оплачен")
def is_paid(modeladmin, request, queryset):
    queryset.update(is_paid = True)

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name_client', 'email', 'phone', 'address', 'date_registered',]
    search_fields = ['name_client',]
    search_help_text = 'Поиск по полю имени клиента'
    list_filter = ['date_registered',]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_product', 'quantity', 'price']
    ordering = [ 'name_product', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['name_product', 'description']
    search_help_text = 'поиск продукции по наименованию'
    actions = [reset_quantity]
    readonly_fields = ['date_added']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name_product'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'описание товара',
                'fields': ['description'],
            },
        ),
        (
            'бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            },
        ),

    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer',  'total_price', 'is_paid']
    ordering = [ '-id']
    list_filter = ['date_ordered', 'total_price', 'is_paid']
    search_fields = ['date_ordered']
    search_help_text = 'поиск заказа дате'
    actions = [is_paid]
    readonly_fields = ['date_ordered']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Продукция',
            {
                'classes': ['collapse'],
                'description': 'продукция',
                'fields': ['products'],
            },
        ),
        (
            'бухгалтерия',
            {
                'fields': ['total_price', 'is_paid', ],
            },
        ),

    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)