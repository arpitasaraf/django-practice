from django.shortcuts import render
from basic.models import Blog
# Create your views here.

def home_view(request):
    data = Blog.objects.all()
    # print(data.values())
    dict = {
        "blogs" : data
    }
    return render(request,'basic/blogCard.html',context=dict)


def create_blog_view(request):
    return render(request,'basic/createblog.html')


def blog_content_view(request):
    return render(request,'basic/blogContent.html')