
from django.contrib import admin
from django.urls import path
from registration.views import contact_form_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-form/',contact_form_view,name="contact_form_view")
]
