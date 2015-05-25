from django.conf.urls import url, patterns

urlpatterns = patterns(
    'aikidoleoni.blog.views',
    url(r'^$', 'posts_list', name='posts_list'),
    url(r'^(?P<slug>[\w\-_]+)/$',
        'post_detail', name='posts_list'),
)
