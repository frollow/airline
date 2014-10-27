from django.conf.urls import patterns, include, url

import flight.views

from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'airline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^flights/', flight.views.ListFlightView.as_view(), name='flights',),

    url(r'^$', 'flight.views.index'),
    # url(r'^$', RedirectView()), to flight
)
