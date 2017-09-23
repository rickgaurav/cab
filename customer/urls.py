from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from customer import views

app_name = 'customer'
urlpatterns = [
    url(r'^$', views.customer_app, name='customer_app'),
    url(r'^customers/$', views.CustomerList.as_view(), name='list'),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view(), name='detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
