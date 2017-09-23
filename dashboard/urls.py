from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^trips/$', views.TripList.as_view(), name='trip_list'),
    url(r'^trips/(?P<pk>[0-9]+)/$', views.TripDetail.as_view(), name='trip_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
