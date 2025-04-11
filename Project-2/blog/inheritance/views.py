from django.shortcuts import render

# Create your views here.

def about_page_view(request):
    return render(request,"inheritance/about-page.html")

def contact_page_view(request):
    return render(request,"inheritance/contact-page.html")

def personal_page_view(request):
    return render(request,"inheritance/personal-page.html")

def complain_page_view(request):
    return render(request,"inheritance/complain-page.html")