# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_shedule_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shedule',
            old_name='carwash_id',
            new_name='flat_id',
        ),
    ]
