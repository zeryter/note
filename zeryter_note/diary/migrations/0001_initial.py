# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('creat_time', models.DateTimeField(default=datetime.datetime(2015, 11, 7, 3, 48, 20, 939027, tzinfo=utc))),
                ('refresh_time', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('text', models.TextField(max_length=20000)),
                ('auther', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
