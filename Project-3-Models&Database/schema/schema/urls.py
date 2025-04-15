
from django.contrib import admin
from django.urls import path
from product.views import all_product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-products/',all_product_view,name = 'all_product_view')
]
