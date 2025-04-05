
from django.urls import path
from order.views import order_view,contact_view,about_view,product_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("order/",order_view),
    path("contact/",contact_view),
    path("about/",about_view),
    path("product/",product_view)
]
