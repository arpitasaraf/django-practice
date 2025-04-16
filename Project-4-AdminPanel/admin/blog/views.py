from django.shortcuts import render
from blog.models import Blog
from articles.models import Article
# Create your views here.

def blog_view(request):
    data = Article.objects.all()
    print(data)
    d = {
        "articles" : data
    }
    return render(request,"blog/index.html",context=d)