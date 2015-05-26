from django.shortcuts import render, get_object_or_404
from aikidoleoni.core.models import Page
from aikidoleoni.blog.models import Post

def home(request):
    template = "core/home.html"
    page = get_object_or_404(Page, slug='home')
    context = dict(
        page=page,
        posts=[Post()]*3
    )
    return render(request, template, context)


def contact(request):
    page = get_object_or_404(Page, slug='contato')
    context = dict(
        page=page,
    )
    template = "core/contact.html"
    return render(request, template, context)


def about(request):
    page = get_object_or_404(Page, slug='sobre')
    context = dict(
        page=page,
    )
    template = "core/about.html"
    return render(request, template, context)


def about_aikido(request):
    page = get_object_or_404(Page, slug='sobre-o-aikido')
    context = dict(
        page=page,
    )
    template = "core/about.html"
    return render(request, template, context)

