from django.conf.urls import url, patterns

urlpatterns = patterns(
    'aikidoleoni.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
    url(r'^sobre/$', 'about', name='about'),
    url(r'^sobre-o-aikido/$', 'about_aikido', name='about_aikido'),
)
