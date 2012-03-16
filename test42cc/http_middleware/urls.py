from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('http_middleware.views',
    url('^$', 'requests', name='requests')
)
