from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.core.management.base import BaseCommand, CommandError

#from django_mqtt.publisher.models import * 

#from django_mqtt.publisher.models import *

def on_connect(client, userdata, flags, rc):
    print ("Hi", client._client_id, userdata, flags, rc)


def on_disconnect(client, userdata, rc):
    print ("Bye", client._client_id, userdata, rc)


def on_message(client, userdata, message):
    print ("Msg", client._client_id, userdata)
    print ("mid", message.mid, "dup:", message.dup, "QoS:", message.qos)
    print ("retain", message.retain, "state", message.state)
    print ("timestamp", message.timestamp)
    print ("topic", message.topic)
    print ("payload", message.payload)
    print ("=============================")


def on_publish(client, userdata, mid):
    print ("Publish", client._client_id, userdata, mid)


def on_subscribe(client, userdata, mid, granted_qos):
    print ("Subscribe", client._client_id, userdata, mid, granted_qos)


def on_unsubscribe(client, userdata, mid):
    print ("Unsubscribe", client._client_id, userdata, mid)


def on_log(client, userdata, level, buf):
    print ("Log", client._client_id, userdata, level, buf)


class Command(BaseCommand):
    help = _('Connect with client as subscriber, for test proposed')

    def add_arguments(self, parser):
        parser.add_argument('topic', action='store',
                            type=str, default=None,
                            help=unicode(_('Sibcribe topic'))
                            )
        parser.add_argument('--id', nargs=1, action='store',
                            type=int, default=None, dest='id',
                            help=unicode(_('id from DB object'))
                            )
        parser.add_argument('--qos', nargs=1, action='store',
                            type=int, default=0, dest='qos',
                            help=unicode(_('Quality of Service'))
                            )
        parser.add_argument('--client_id', nargs=1, action='store',
                            type=str, default=None, dest='client_id',
                            help=unicode(_('client_id for broken'))
                            )

    def handle(self, *args, **options):
        if not options['topic']:
            raise CommandError(unicode(_('Topic requiered and must be only one')))
        filter = {}
        id = options['id']
        if options['id'] is None:
            if options['client_id']:
                filter['client_id'] = options['client_id']
            clients = Client.objects.filter(**filter)
            if clients.count() == 1:
                id = clients.all()[0].pk
            else:
                if clients.all().count() == 0:
                    raise CommandError(unicode(_('No client on DB')))
                print ('id -> client')
                for obj in clients.all():
                    print (obj.pk, '->', obj)
                id = input("Select id from DB: ")
        try:
            obj = Client.objects.get(pk=id)
            cli = obj.get_mqtt_client()

            cli.on_connect = on_connect
            cli.on_disconnect = on_disconnect
            cli.on_publish = on_publish
            cli.on_subscribe = on_subscribe
            cli.on_unsubscribe = on_unsubscribe
            cli.on_message = on_message
            cli.on_log = on_log
            cli.connect(obj.server.host, obj.server.port, obj.keepalive)
            cli.subscribe(options['topic'], options['qos'])
            cli.loop_forever()
            cli.disconnect()
        except Client.DoesNotExist:
            raise CommandError(unicode(_('Client not exist')))

