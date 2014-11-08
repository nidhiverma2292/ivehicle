from django.conf.urls import patterns, include, url
from django.contrib import admin
from car_details.views import index

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'car_details.views.index', name='home'),
    url(r'^(?P<id>\d+)$', 'car_details.views.car_detail', name='details'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
