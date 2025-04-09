from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def article_page_view(request):
    
    return HttpResponse("Begin a new session")

def article_writer_view(request , **kwargs):
    city = kwargs.get("city")
    state = kwargs.get("state")    
    return HttpResponse(f"write a any summary.about the city:{city},inside the state: {state}.")

def article_read_view(request):
    dict = {
        "name": "Hamza",
        "site_name": "My Django Site",
        "id": 123456789,
        "role" : "senior",
        "skills": ["Python", "Django", "JavaScript", "HTML", "CSS"],
        "isGraduated": True,
          "country_info" : {
            "country" : "India",
            "capital" : "New Delhi",
            "currency" : "INR",
            "population" :  1460634340,
        }
    }
    return render(request,"articles/index.html",context=dict)


def article_filter_view(request):
    dict = {
        "name": "Hamza",
        "site_name": "MY DJANGO SITE".lower(),
        "id": 123456789,
        "role" : "senior",
        "desc" : "I am mohd hamza. I teach at SRB Institute",
        "adhaarNo" : None
    }
    return render(request,"articles/filter.html",context=dict)