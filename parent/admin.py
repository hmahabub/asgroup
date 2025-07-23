from django.contrib import admin
from .models import Company, ProductCategory, Product, Review, ContactInfo

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'website_url', 'created_at']
    search_fields = ['name', 'description']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'company', 'price_min', 'price_max', 'is_active']
    list_filter = ['category', 'company', 'is_active']
    search_fields = ['title', 'description']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'company', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'company', 'is_featured']
    search_fields = ['author_name', 'review_text']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()