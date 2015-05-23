from django.conf.urls import url, patterns

urlpatterns = patterns(
    'aikidoleoni.core.views',
    url(r'^$', 'home', name='home'),
)
