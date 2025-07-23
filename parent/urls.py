from django.urls import path
from . import views

app_name = 'parent'

urlpatterns = [
    path('', views.index, name='index'),
    path('sourcequest/', views.sourcequest, name='sourcequest'),
    path('anomyo/', views.anomyo, name='anomyo'),
    path('api/filter-products/', views.filter_products, name='filter_products'),
]