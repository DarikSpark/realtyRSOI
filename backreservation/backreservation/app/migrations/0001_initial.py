# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('flat_id', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('busy_from', models.TimeField()),
                ('busy_to', models.TimeField()),
            ],
        ),
    ]
