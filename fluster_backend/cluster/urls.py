from django.conf.urls import patterns, url
from cluster import views
urlpatterns = patterns(
    'users.views',
    url(
        regex=r'^$',
        view='launch_clustering',
        name='basic_urls',
    ),
)
