from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(max_age=300)
@require_http_methods(["GET"])
def index(request):
    template = "blog/landing.html"
    blogs = Blog.objects.all().order_by("-created_at")[:2]
    return render(request, template, { "blogs": blogs})


@cache_control(max_age=300)
@require_http_methods(["GET"])
def blog_list_view(request):
    blogs = Blog.objects.all()
    template = "blog/blog_list.html"
    return render(request, template, { "blogs": blogs })


@cache_control(max_age=300)
@require_http_methods(["GET"])
def blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    template = "blog/blog.html"
    return render(request, template, { "blog": blog})
    