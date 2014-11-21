from django.conf.urls import patterns, include, url

import flight.views
import flight.forms

from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^flights/', flight.views.ListFlightView.as_view(), name='flights', ),
                       url(r'^$', flight.views.index),
                       url(r'^search/$', flight.views.search),
                       url(r'^search_results/$', flight.views.search),
                       url(r'^blog/', include('blog.urls')),
                       #url(r'^fill_data/([0-9])$', )

)
