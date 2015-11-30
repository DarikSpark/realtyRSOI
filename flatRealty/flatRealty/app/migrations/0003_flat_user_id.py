# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151029_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
