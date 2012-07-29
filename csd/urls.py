# -*- coding: utf-8 *-*
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from programas import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^programas/(?P<perfil>\w+)/(?P<lugar>\w+)/$', views.ProgramasListView.as_view(), name='programas'),
    url(r'^ver-programa/(?P<programa_id>\d+)/$', views.ver_programa, name='ver_programa'),
    url(r'^redactar/$', views.redactar, name='redactar'),
    url(r'^gracias/$', views.redactar_gracias, name='redactar_gracias'),
    #url(r'^productos/', views.ProductosListView.as_view(), name='productos'),
    #url(r'^contacto/', views.contacto, name='contacto'),
    #url(r'^novedades/', views.NovedadesListView.as_view(), name='novedades'),

    url(r'^admin/', include(admin.site.urls)),

)
  

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )

urlpatterns += staticfiles_urlpatterns()
