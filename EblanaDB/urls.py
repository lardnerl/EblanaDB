from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
import database.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EblanaDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', database.views.ListCharacterView.as_view(),
        name='character-list',),
    url(r'^new$', database.views.CreateCharacterView.as_view(),
    name='character-new',),
    url(r'^eblana/', include('database.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<pk>\d+)/$', database.views.CharacterView.as_view(),
        name='character-view',),
    url(r'^edit/(?P<pk>\d+)/$', database.views.UpdateCharacterView.as_view(),
        name='character-edit',),

)

urlpatterns += staticfiles_urlpatterns()