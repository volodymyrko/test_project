from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('contact.views',
    url('^$', 'index', name='index'),
    url('^edit/$', 'edit', name='edit'),
)