from django.shortcuts import render

# Create your views here.
def ui_view(request):
    return render(request,"ui/index.html")