from django.contrib import admin
from django.urls import path
from registration.views import registration_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',registration_view)
]
