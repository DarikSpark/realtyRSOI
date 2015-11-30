# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_flat_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flat',
            name='rooms',
            field=models.IntegerField(default=0),
        ),
    ]
