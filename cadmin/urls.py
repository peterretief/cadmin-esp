from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.request_list, name='request_list'),
]
