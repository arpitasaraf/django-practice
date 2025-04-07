
from django.urls import path
from order.views import order_view,contact_view,about_view,product_view,home_view
from blog.views import home_blog_view,single_blog_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path(route, view, kwargs=None, name=None) Syntax
    path("",home_view,kwargs={"name":"Alex","city":"Allahabad","page" : "Home-Page"},name = "home_view"),
    path("order/",order_view),
    path("contact/",contact_view),
    path("about/",about_view),
    path("product/",product_view),
    path("home-blog/",home_blog_view,name="home-blog-view"),
    path("single-blog/",single_blog_view)
]
