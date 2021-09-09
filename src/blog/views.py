from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost


def blog_post_detail_page(request, slug):
    """
    try:
        obj = BlogPost.objects.get(slug=post_id)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    """
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() == 0:
        raise Http404
    else:
        obj = queryset.first()
    #obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)
