from django.conf.urls import url, patterns

urlpatterns = patterns(
    'core.views',
    url(r'^$', 'home', name='home'),
)
