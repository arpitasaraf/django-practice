from django.shortcuts import render
from registration.forms import ContactForm, SignupForm
from django.http import HttpResponseRedirect


def contact_form_view(request):
    fm = ContactForm(auto_id="hamza_%s", label_suffix=":------",
                     initial={"first_name": "Mohd", "last_name": "Hamza"},
                     field_order=['age', 'first_name', 'email', 'last_name']
                     )
    dict = {
        "form": fm
    }
    return render(request, 'registration/index.html', context=dict)


def signup_view(request):
    # print(request)
    # print(request.__dict__)
    # print("request methhhod : ",request.method)
    if request.method == "POST":
        # print(request.POST)
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(name, email, password)
        # return HttpResponseRedirect("/success-signup/")
        return HttpResponseRedirect("/signup/")

    fm = SignupForm()
    dict = {"form": fm}
    return render(request, "registration/signup.html", context=dict)


def success_page_view(request):
    return render(request, "registration/signupSuccess.html")


def home_view(request):
    return render(request, "registration/home.html")
