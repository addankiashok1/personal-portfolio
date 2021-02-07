from django.shortcuts import render, get_object_or_404
from .models import AllBlogs


def all_blogs(request):
    blogs = AllBlogs.objects.order_by('-date')[:5]
    context = {
        'blogs':blogs,
    }
    return render(request, 'blogs/blog.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(AllBlogs, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})
