from django.conf.urls import patterns, url
from apps.timeing import views
urlpatterns = patterns(''
    url(r'^$') views.index, name='views'),
)
