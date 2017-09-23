from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from driver import views

urlpatterns = [
    url(r'^drivers/$', views.DriverList.as_view()),
    url(r'^drivers/(?P<pk>[0-9]+)/$', views.DriverDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
