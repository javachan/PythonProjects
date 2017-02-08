from django.conf.urls import patterns, include, url
from DJangoSample.views import hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    # Examples:
    # url(r'^$', 'DJangoSample.views.home', name='home'),
    # url(r'^DJangoSample/', include('DJangoSample.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
