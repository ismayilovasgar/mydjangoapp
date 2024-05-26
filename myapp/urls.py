from django.urls import path
from .views import index, blogs, blog_details

urlpatterns = [
    path("", index),
    path("index/", index),
    path("blogs/", blogs),
    path("blogs/<int:id>", blog_details),
]
