

from django.contrib import admin
from django.urls import path
from articles.views import article_page_view, article_writer_view, article_read_view, article_filter_view, article_date_view
from design.views import design_view
from ui.views import ui_view
from layout.views import home_view
from inheritance.views import about_page_view, contact_page_view, personal_page_view, complain_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', article_page_view, name="article_page_view",
         kwargs={"name": "navansh", "isMale": True}),
    path('articles-write/', article_writer_view, name="article_writer_view",
         kwargs={"city": "kanpur", "state": "U.P."}),
    path("article-read/", article_read_view, name="article_read_view"),
    path("django-filters/", article_filter_view, name="article-filter-view"),
    path("django-date/", article_date_view, name="article-date-view"),
    path("django-static-files/", design_view, name="design_view"),
    path("django-static-ui-view/", ui_view, name="ui_view"),
    path("", home_view,name="home_view"),
    path("django-about-page/", about_page_view,name="about_page_view"),
    path("contact-page/", contact_page_view),
    path("personal-page/", personal_page_view,name = "personal_page_view"),
    path("complain-page/", complain_page_view),
]
