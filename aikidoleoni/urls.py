from django.conf.urls import include, url
from django.contrib import admin
from aikidoleoni import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('core.urls', namespace='core')),
]