from django.contrib import admin

from catalog.models import Category, Product, CompanyContact, UserQuestion, Delivery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(CompanyContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_name', 'phone', 'email', 'question',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'delivery_number', 'delivery_date', 'is_current')
