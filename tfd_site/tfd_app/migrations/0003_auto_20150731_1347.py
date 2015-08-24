# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfd_app', '0002_strain_strain_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strain',
            name='strain_info',
            field=models.TextField(max_length=1080),
        ),
    ]
