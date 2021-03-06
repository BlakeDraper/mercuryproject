from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^mercuryadmin/', include(admin.site.urls)),
    url(r'^mercuryservices/', include('mercuryservices.urls')),# namespace="mercuryservices")),
    url(r'^mercurydocs/', include('rest_framework_swagger.urls')),
    url(r'^mercurylab/', include('mercurylab.urls', namespace="mercurylab")),
)
