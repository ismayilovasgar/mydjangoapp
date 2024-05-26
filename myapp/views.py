from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # return HttpResponse("home page")
    return render(request, "blog/index.html")


def blogs(request):
    return render(request, "blog/blogs.html")


def blog_details(request, id):
    # return HttpResponse("blog details:" + str(id))
    # return HttpResponse(f"blog details: {id}")
    return render(request, "blog/blog_details.html", {"id": id})
