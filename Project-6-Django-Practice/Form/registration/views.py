from django.shortcuts import render

# Create your views here.
def registration_view(requests):
    dict = {
        "name": "Hamza",
        "site_name": "My Django Site",
        "id": 123456789,
        "skills": ["Python", "Django", "JavaScript", "HTML", "CSS"],
        "isGraduated": True,
          "country_info" : {
            "country" : "India",
            "capital" : "New Delhi",
            "currency" : "INR",
            "population" :  1460634340,
        }
    }
    return render(requests,"registration/index.html",context=dict)