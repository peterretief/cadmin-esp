from django.shortcuts import render
from django.utils import timezone

#from django_mqtt.publisher.models import *
from django_mqtt.publisher.signals import *
#from django mqtt.server.models import *

from django_mqtt.publisher.models import *
from django.core.files import File
from django.test import TestCase
import os

from django.db.models.signals import post_save
from django_mqtt.publisher.models import Data as MQTTData

#def update_mqtt_data(sender, **kwargs):
#    obj = kwargs["instance"]
#    if isinstance(obj, MQTTData):
#        if kwargs["created"]:
#            obj.update_remote()
#post_save.connect(receiver=update_mqtt_data, sender=MQTTData, dispatch_uid='django_mqtt_update_signal')


def connect_localhost():
#      client_id = ClientId.objects.get(name='test1client').first()
       #server = Server.objects.all()[0]
       print(MQTTData)
       client_id = ClientId.objects.all()[0]
       server = Server.objects.filter(host='localhost', port=1883)
#      client = Client.objects.create(server=server, clean_session=False)

       topic = Topic.objects.filter(name='/test/publish')
#       update_mqtt_data("some data")       


#def before_connect(sender, client):
#    if not isinstance(client, Client):
#        raise AttributeError('client must be Client object')
#mqtt_connect.connect(receiver=before_connect, sender=Server, dispatch_uid='my_django_mqtt_before_connect')

#def before_publish(sender, client, topic, payload, qos, retain):
#    if not isinstance(client, Client):
#        raise AttributeError('client must be Client object')
#mqtt_pre_publish.connect(receiver=before_publish, sender=Data, dispatch_uid='my_django_mqtt_before_publish')

#def then_publish(sender, client, userdata, mid):
#    if not isinstance(client, Client):
#        raise AttributeError('client must be Client object')
#mqtt_publish.connect(receiver=then_publish, sender=Client, dispatch_uid='my_django_mqtt_then_publish')

#def then_disconnect(sender, client, userdata, rc):
#    if not isinstance(client, MQTTClient):
#        raise AttributeError('client must be MQTTClient object')
#mqtt_disconnect.connect(receiver=then_disconnect, sender=Server, dispatch_uid='my_django_mqtt_then_disconnect')

def mqtt_list(mqtt):
    topics = Topic.objects.all() 	
    connect_localhost()

  #  requests = Request.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(mqtt, 'django_mqtt/mqtt_list.html', {"topics":topics})


