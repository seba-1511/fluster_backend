from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^admin/', include(admin.site.urls)),
    url(
        r'^users/',
        include('users.urls')
    ),
    url(
        r'^cluster/',
        include('cluster.urls')
    ),
)
