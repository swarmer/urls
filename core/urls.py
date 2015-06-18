from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views


urlpatterns = patterns('core.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/admin/', permanent=False)),

    url(r'^([\w-]+)$', views.url),
)
