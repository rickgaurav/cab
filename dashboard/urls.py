from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dashboard import views

urlpatterns = [
    url(r'^trips/$', views.TripList.as_view()),
    url(r'^trips/(?P<pk>[0-9]+)/$', views.TripDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
