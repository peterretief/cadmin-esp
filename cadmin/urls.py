from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.request_list, name='request_list'),
    url(r'^print_test/$', views.print_test,  name='request_print'),
]
