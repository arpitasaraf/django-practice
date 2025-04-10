"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles.views import article_page_view , article_writer_view,article_read_view,article_filter_view,article_date_view
from design.views import design_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',article_page_view,name="article_page_view",kwargs={"name":"navansh","isMale":True}),
    path('articles-write/',article_writer_view, name="article_writer_view",kwargs={"city":"kanpur","state":"U.P."}),
    path("article-read/",article_read_view,name="article_read_view"),
    path("django-filters/",article_filter_view,name="article-filter-view"),
    path("django-date/",article_date_view,name="article-date-view"),
    path("django-static-files/",design_view,name="design_view")
]
