from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^admin/', include(admin.site.urls)),
    url(
        r'^apiv1/',
        include('users.urls')
    ),
)
