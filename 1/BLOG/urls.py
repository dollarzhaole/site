from django.conf.urls import patterns, include, url
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BLOG.views.home', name='home'),
    # url(r'^BLOG/', include('BLOG.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sblog/', include('sblog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/',include('grappelli.urls')),
)

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns((''),
(r'^static/(?P<path>.*)$', 'django.views.static.serve',
 {'document_root': settings.STATIC_ROOT}
),
)
