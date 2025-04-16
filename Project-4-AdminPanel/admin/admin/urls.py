
from django.contrib import admin
from django.urls import path
from blog.views import blog_view

urlpatterns = [
    path('admin/', admin.site.urls), # private 
    # blog urls
    path('blog/',blog_view,name="blog_view")




    # product urls 
]
