from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    title = "Hello there..."
    context = {"title": title, "my_list": [1, 2, 3, 4, 5]}
    # doc = "<h1>{title}</h1>".format(title=title)
    # django_render_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About us"})


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    render_item = template_obj.render(context)
    return HttpResponse(template_obj.render(context))


def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact us"})
