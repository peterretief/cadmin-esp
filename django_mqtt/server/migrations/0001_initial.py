# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 09:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_mqtt', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qos', models.IntegerField(choices=[(0, 'QoS 0: Delivered at most once'), (1, 'QoS 1: Always delivered at least once'), (2, 'QoS 2: Always delivered exactly once')], default=0)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_mqtt.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remain', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('message', models.BinaryField(blank=True, null=True)),
                ('packet_id', models.IntegerField(default=-1)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('init_conn', models.DateTimeField(auto_now_add=True)),
                ('last_conn', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('keep_alive', models.IntegerField(default=0)),
                ('client_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_mqtt.ClientId')),
                ('subscriptions', models.ManyToManyField(to='server.Channel')),
                ('unsubscriptions', models.ManyToManyField(to='django_mqtt.Topic')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='publication',
            unique_together=set([('channel', 'remain')]),
        ),
        migrations.AlterUniqueTogether(
            name='channel',
            unique_together=set([('qos', 'topic')]),
        ),
    ]
