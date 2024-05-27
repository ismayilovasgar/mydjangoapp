from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
data = {
    "blogs": [
        {
            "id": 1,
            "title": "Komple Web Gelistirme Kursu",
            "image": "1.jpg",
            "is_active": True,
            "is_home": False,
            "description": "cok iyi kurs tavsiye ederim",
        },
        {
            "id": 2,
            "title": "Front-End Gelistirme Kursu",
            "image": "2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "yeni baslayanlar icin degil",
        },
        {
            "id": 3,
            "title": "Back-End Gelistirme Kursu",
            "image": "3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "sifirdan baslayanlar icin",
        },
    ]
}


def index(request):
    context = {
        "blogs": data["blogs"],
    }
    # return HttpResponse("home page")
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": data["blogs"],
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    # return HttpResponse("blog details:" + str(id))
    # return HttpResponse(f"blog details: {id}")
    blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    selectedBlog = [blog for blog in blogs if blog["id"] == id][0]
    return render(request, "blog/blog_details.html", {"blog": selectedBlog})
