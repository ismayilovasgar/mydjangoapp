from django.urls import path
from .views import blogs_by_category, index, blogs, blog_details

urlpatterns = [
    path("", index, name="home"),
    path("index/", index),
    path("blogs/", blogs, name="blogs"),
    path("category/<slug:slug>", blogs_by_category, name="blogs-by-category"),
    path("blogs/<slug:slug>", blog_details, name="blog_details"),
]
