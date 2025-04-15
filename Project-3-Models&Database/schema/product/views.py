from django.shortcuts import render
from product.models import Products
# Create your views here.


def all_product_view(request):
    data = Products.objects.all() # fetch all products
    print(data) # returns a queryset which means data returned from database
    dict = {
        "products" : data
    }
    # show = data.values()
    # print(show)
    return render(request,'product/index.html',context=dict)
