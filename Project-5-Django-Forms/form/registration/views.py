from django.shortcuts import render
from registration.forms import ContactForm


def contact_form_view(request):
    fm = ContactForm(auto_id="hamza_%s", label_suffix=":------",
                     initial={"first_name": "Mohd", "last_name": "Hamza"},
                     field_order=['age','first_name','email','last_name']
                     )
    dict = {
        "form": fm
    }
    return render(request, 'registration/index.html', context=dict)
