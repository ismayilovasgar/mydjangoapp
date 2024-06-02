from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Blog, Category

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
        # "blogs": data["blogs"],
        # "blogs": Blog.objects.all(),
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all(),
    }
    # return HttpResponse("home page")
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        # "blogs": data["blogs"],
        # "blogs": Blog.objects.all(),
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all(),
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    # return HttpResponse("blog details:" + str(id))
    # return HttpResponse(f"blog details: {id}")
    # blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    # selectedBlog = [blog for blog in blogs if blog["id"] == id][0]
    blog = Blog.objects.get(slug=slug)
    # return render(request, "blog/blog_details.html", {"blog": selectedBlog})
    return render(request, "blog/blog_details.html", {"blog": blog})


def blogs_by_category(request, slug):
    context = {
        # ManyToOne
        # "blogs": Blog.objects.filter(is_active=True, category_id__slug=slug),
        # ManyToOne
        # "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        # ManyTomany
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug,
    }
    return render(request, "blog/blogs.html", context)
