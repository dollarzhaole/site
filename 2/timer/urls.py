from django.conf.urls import patterns, include, url

urlpatterns = patterns('timer.views',
                       url(r'^checkin/$', 'check_in', name='checkin'),
                       )
