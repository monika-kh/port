from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog


def index(request):
    blog = Blog.objects.all()
    context = {"blog": blog}
    return render(request, "blogs/index.html", context)


def detail(request, blog_id):
    blog_data = Blog.objects.all()
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blogs/detail.html", {"blog": blog, "blogs": blog_data})
