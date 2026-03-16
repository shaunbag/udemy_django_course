from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_control
from django.http import HttpResponseNotFound

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
def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    template = "blog/blog.html"
    if not blog:
        return HttpResponseNotFound(render(request, "404.html"))
    else:
        return render(request, template, { "blog": blog})
    