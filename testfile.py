from django_mqtt.publisher.models import *

client_id = ClientId.objects.create(name='publisher')
server = Server.objects.get(host='localhost', port=1883)
client = Client.objects.create(server=server, clean_session=True, client_id=client_id)
topic = Topic.objects.get(name='/test/publish')
for qos in [MQTT_QoS0, MQTT_QoS1, MQTT_QoS2]:
	data, is_new = Data.objects.get_or_create(client=client, topic=topic)
	data.qos = qos
	data.payload = bytes('test %(qos)s' % {'qos': qos}, 'UTF-8')
	data.retain = True
	data.save()
	data.update_remote()

server = Server.objects.get(pk=server.pk)
server.save()

client = Client.objects.get(pk=client.pk)
client.save()

