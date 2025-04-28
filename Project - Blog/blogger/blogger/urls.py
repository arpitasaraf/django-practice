
from django.contrib import admin
from django.urls import path
from basic.views import home_view,create_blog_view,blog_content_view
urlpatterns = [
    path('admin/', admin.site.urls),
    # basic
    path('',home_view,name="home_view"),
    path('create-blog/',create_blog_view,name="create_blog_view"),
    path('blog-content/',blog_content_view,name="blog_content_view")
]
