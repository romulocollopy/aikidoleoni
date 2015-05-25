from django.shortcuts import render


def home(request):
    template = "core/home.html"
    return render(request, template)


def contact(request):
    template = "core/contact.html"
    return render(request, template)


def about(request):
    template = "core/about.html"
    return render(request, template)


def about_aikido(request):
    template = "core/about.html"
    return render(request, template)

