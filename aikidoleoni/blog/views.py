from django.shortcuts import render, get_object_or_404
from aikidoleoni.core.models import Page
from aikidoleoni.blog.models import Post

# Create your views here.
def posts_list(request):
    page = get_object_or_404(Page, slug='blog')
    context = dict(
        page=page,
        posts=Post.published_posts.all()
        )
    template = "blog/posts_list.html"
    return render(request, template, context)


def post_detail(request, slug):
    page = get_object_or_404(Page, slug='blog')
    post = get_object_or_404(Post, slug=slug)
    context = dict(
        post=post,
        page=page
        )
    template = "blog/post_detail.html"
    return render(request, template, context)
