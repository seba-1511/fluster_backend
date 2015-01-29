from django.conf.urls import patterns, url
from cluster import views
urlpatterns = patterns(
    'cluster.views',
    url(
        regex=r'^(?P<token>.+)$',
        view='launch_clustering',
        name='basic_urls',
    ),
)
