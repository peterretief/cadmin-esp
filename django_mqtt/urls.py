from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.mqtt_list, name='mqtt_list'),
#    url(r'^mqtt/', include('django_mqtt.mosquitto.auth_plug.urls')),
]

