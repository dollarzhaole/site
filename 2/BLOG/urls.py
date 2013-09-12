from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BLOG.views.home', name='home'),
    # url(r'^BLOG/', include('BLOG.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site/', include('sblog.urls')),
    url(r'^timer/', include('timer.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'', 'sblog.views.index', name='index'),
    )
urlpatterns += patterns((''),
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.STATIC_ROOT}
                        ),
                        )
