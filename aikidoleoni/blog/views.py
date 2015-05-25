from django.shortcuts import render

# Create your views here.
def posts_list(request):
    template = "blog/posts_list.html"
    return render(request, template)


def post_detail(request, slug):
    template = "blog/post_detail.html"
    return render(request, template)
