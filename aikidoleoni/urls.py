from django.conf.urls import include, url
from django.contrib import admin
from aikidoleoni import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^publica[çc][õo]es/',
        include('aikidoleoni.blog.urls', namespace='blog')),
    url(r'^', include('aikidoleoni.core.urls', namespace='core')),
]