from django.shortcuts import render
from basic.models import Blog
from basic.forms import BlogForm
from django.http import HttpResponseRedirect


def home_view(request):
    data = Blog.objects.all()
    # print(data.values())
    dict = {
        "blogs" : data
    }
    return render(request,'basic/blogCard.html',context=dict)


def create_blog_view(request):
    # print(request.method)
    if request.method == "POST":
        print(request.POST)
        fm = BlogForm(request.POST)
        # print(fm)
        if fm.is_valid(): # validate form at server side
             print("create somse data")
            #  print(fm.cleaned_data)
             title = fm.cleaned_data.get('title')
             content = fm.cleaned_data.get('content')
             is_published = fm.cleaned_data.get('is_published')
             create_data = Blog.objects.create(
                 title = title,
                 content = content,
                 is_published = is_published
             )
             print(create_data.__dict__)
             return HttpResponseRedirect(f'/blog-content/{create_data.id}')
    else:
        fm = BlogForm()

    context = {
        "form" : fm
    }
    return render(request,'basic/createblog.html',context=context)


def blog_content_view(request,blog_id):
    print(blog_id)
    data = Blog.objects.get(id=blog_id)
    # print(data.__dict__)
    context = {
        "blog" : data
    }
    return render(request,'basic/blogContent.html',context=context)

