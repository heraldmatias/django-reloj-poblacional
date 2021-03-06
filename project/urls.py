from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       (r'^', include('inei.reloj.urls'))
)

if settings.DEBUG:
    from django.views.static import serve

    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                            url(r'^static/(?P<path>.*)$',
                                serve, {'document_root': settings.STATIC_ROOT})
    )