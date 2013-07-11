from django.conf.urls import patterns, include, url

urlpatterns = patterns('sblog.views',
                       url(r'^bloglist/$', 'blog_list', name='bloglist'),
                       url(r'^blog/(?P<id>\d+)/$', 'blog_show', name='detailblog'),
                       url(r'^blog/tag/(?P<id>\d+)/$', 'blog_filter', name='filtrblog'),
                       # url(r'^blog/add/$', 'blog_add', name='addblog'),
                       # url(r'^blog/(?P<id>\w+)/del/$', 'blog_del', name='delblog'),
                       url(r'^blog/(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='showcomment'),
                       url(r'^blog/tag/(?P<id>\d+)/$', 'blog_filter', name='filterblog'),
                       # url(r'^commentslist/$', 'blog_show_comment_list', name='comment_list'),
                       )
