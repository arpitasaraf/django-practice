from django.http import HttpResponse

def home_view(request,**kwargs):
    print(kwargs)
    name = kwargs.get("name")
    city = kwargs.get("city")
    page = kwargs.get("page")
    return HttpResponse(f"This is home page. name = {name} , city = {city}. Page = {page}")

def order_view(request):
    totalProduct = 100
    response = f"Welcome to order page. Total products = {totalProduct}"
    return HttpResponse(response)

def contact_view(request):
    return HttpResponse("This is Contact Page")

def about_view(request):
    
    return HttpResponse("<h1><u>This is about page</u></h1>")

def product_view(request):
    return HttpResponse("product item list")