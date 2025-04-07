from django.shortcuts import render

# Create your views here.


def home_blog_view(request):
    return render(request, "blog/index.html", context={"name": "Hamza", "id": 329239, "isMale": True})


def single_blog_view(request):
    dict = {
        "blogName": "aradhya",
        "isFemale": True
    }
    return render(request, "blog/blog.html", context=dict)
