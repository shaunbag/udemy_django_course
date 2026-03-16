from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blogs/", views.blog_list_view, name="blog-list"),
    path("blog/<slug:slug>/", views.blog, name="blog")
]