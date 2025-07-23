from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Company, Product, ProductCategory, Review, ContactInfo

def index(request):
    companies = Company.objects.all()
    featured_products = Product.objects.filter(is_active=True)[:6]
    categories = ProductCategory.objects.all()
    featured_reviews = Review.objects.filter(is_featured=True)[:3]
    contact_info = ContactInfo.objects.first()
    
    context = {
        'companies': companies,
        'featured_products': featured_products,
        'categories': categories,
        'featured_reviews': featured_reviews,
        'contact_info': contact_info,
    }
    return render(request, 'parent/index.html', context)

def sourcequest(request):
    try:
        company = Company.objects.get(name__icontains='sourcequest')
    except Company.DoesNotExist:
        company = None
    
    products = Product.objects.filter(company=company, is_active=True) if company else []
    categories = ProductCategory.objects.all()
    reviews = Review.objects.filter(company=company) if company else []
    contact_info = ContactInfo.objects.first()
    
    context = {
        'company': company,
        'products': products,
        'categories': categories,
        'reviews': reviews,
        'contact_info': contact_info,
    }
    return render(request, 'parent/sourcequest.html', context)

def anomyo(request):
    try:
        company = Company.objects.get(name__icontains='anomyo')
    except Company.DoesNotExist:
        company = None
    
    reviews = Review.objects.filter(company=company) if company else []
    contact_info = ContactInfo.objects.first()
    
    context = {
        'company': company,
        'reviews': reviews,
        'contact_info': contact_info,
    }
    return render(request, 'parent/anomyo.html', context)

def filter_products(request):
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        products = Product.objects.filter(is_active=True)
    else:
        products = Product.objects.filter(
            category__slug=category, 
            is_active=True
        )
    
    products_data = []
    for product in products:
        products_data.append({
            'title': product.title,
            'category': product.category.name,
            'price_range': product.price_range,
            'image_url': product.image.url if product.image else '',
        })
    
    return JsonResponse({'products': products_data})