from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_published', 'created_at']
    list_filter = ['category', 'is_published', 'created_at']
    search_fields = ['name', 'description', 'category__name']

    @admin.action(description="Опубликовать выбранные товары")
    def publish_products(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'Опубликовано {count} товаров.')

    @admin.action(description="Увеличить цену на 10%%")
    def change_price(self, request, queryset):
        updated = 0
        for product in queryset:
            product.price = product.price * 1.1
            product.save()
            updated += 1
        self.message_user(request, f'Цена увеличена для {updated} товаров.')

    actions = ['publish_products', 'change_price']