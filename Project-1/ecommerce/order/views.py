from django.http import HttpResponse

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