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
    """
    print (DJANGO SAYS, request.method, request.path, request.user)
    """
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() == 0:
        raise Http404
    else:
        obj = queryset.first()
    # obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    # List out objects
    # Could be search
    # BlogPost.objects.filter(title_icontains='string')
    qs = BlogPost.objects.all()  # queryset -> List of python objects
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # Create objects
    # ? use a form
    template_name = "blog/create.html"
    context = {"form": None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail vier
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/retrieve.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/update.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


"""
CRUD

GET -> Retrive / List
POST -> Create / Update / Delete

Create Retrive Update Delte

"""
