# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151108_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedule',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
