# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from carecentres import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    # content urls
    url(r'^(?P<carecentre_slug>[\w\-]+)/$', views.carecentre, name='carecentre'),
    url(r'^events/(?P<carecentre_slug>[\w\-]+)/$', views.events, name='events'),

    url(r'^(?P<carecentre_slug>[\w\-]+)/event/(?P<event_slug>[\w\-]+)/$', views.event, name='event'),

    # Add content urls
    url(r'^/add_carecentre/$', views.add_carecentre, name="add_carecentre"),
    url(r'^(?P<carecentre_slug>[\w\-]+)/add_galleryimage/(?P<pk>\d+)/$', views.add_galleryimage, name="add_galleryimage"),
    url(r'^(?P<carecentre_slug>[\w\-]+)/add_event/$', views.add_event, name="add_event"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)