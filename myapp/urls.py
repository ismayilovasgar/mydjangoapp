from django.urls import path
from .views import index, blogs, blog_details

urlpatterns = [
    path("", index, name="home"),
    path("index/", index),
    path("blogs/", blogs, name="blogs"),
    path("blogs/<slug:slug>", blog_details, name="blog_details"),
]
