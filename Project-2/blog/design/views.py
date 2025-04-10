from django.shortcuts import render

# Create your views here.

def design_view(request):
    return render(request,"design/index.html")