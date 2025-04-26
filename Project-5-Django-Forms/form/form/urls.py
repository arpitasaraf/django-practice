
from django.contrib import admin
from django.urls import path
from registration.views import contact_form_view,signup_view,success_page_view,home_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact-form/',contact_form_view,name="contact_form_view"),
    path('signup/',signup_view,name="signup_view"),
    path('success-signup/',success_page_view,name="success_page_view"),
    path('',home_view,name="home_view")
]
