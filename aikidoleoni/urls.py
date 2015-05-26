from django.conf.urls import include, url
from django.contrib import admin
from aikidoleoni import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^publica[çc][õo]es/',
        include('aikidoleoni.blog.urls', namespace='blog')),
    url(r'^', include('aikidoleoni.core.urls', namespace='core')),
]

from django.conf import settings
from django.views.static import serve

# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
   ]