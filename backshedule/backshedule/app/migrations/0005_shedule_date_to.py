# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151128_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedule',
            name='date_to',
            field=models.DateField(default=b'2015-01-01'),
        ),
    ]
