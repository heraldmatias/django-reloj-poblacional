__author__ = 'holivares'

from django.conf.urls import patterns, url
from inei.reloj.views import IndexView, PopulationView

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^population/ajax/$', PopulationView.as_view(), name='population')
)