from django.contrib import admin
from django.urls import path
from practice.views import demo_form_view
from basic.views import home_view, create_blog_view, blog_content_view, delete_blog_view, update_blog_view,search_blog_view
urlpatterns = [
    path('admin/', admin.site.urls),
    # basic
    path('', home_view, name="home_view"),
    path('create-blog/', create_blog_view, name="create_blog_view"),
    path('blog-content/<int:blog_id>/<str:confirm>',
         blog_content_view, name="blog_content_view"),
    path('delete-blog/<int:blog_id>/', delete_blog_view, name="delete_blog_view"),
    path('update-blog/<int:blog_id>/', update_blog_view, name="update_blog_view"),
    path('search-blog/',search_blog_view,name="search_blog_view"),
    # practice 
    path('demo-form/',demo_form_view,name='demo_form_view')
]
