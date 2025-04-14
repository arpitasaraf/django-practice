from django.shortcuts import render

# Create your views here.
def ui_view(request):
    return render(request,"ui/index.html",context={"phoneNo" : 9933,"email" : "example@gmail.com"})