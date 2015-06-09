from django.shortcuts import render, get_object_or_404
from aikidoleoni.core.forms import ContactForm
from aikidoleoni.core.models import Page
from aikidoleoni.blog.models import Post

def home(request):
    template = "core/home.html"
    page = get_object_or_404(Page, slug='home')
    context = dict(
        page=page,
        posts=Post.published_posts.all()[:3],
    )
    return render(request, template, context)


def contact(request):
    page = get_object_or_404(Page, slug='contato')
    context = dict(
        page=page,
        form = ContactForm()
    )
    template = "core/contact.html"

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            return render(request, template, context)
        try:
            if form.send_mail() > 0:
                context['success'] = "Email enviado com sucesso"
        except ConnectionRefusedError:
            context['success'] = "Desculpe, não foi possível enviar sua \
                    mensagem."

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

