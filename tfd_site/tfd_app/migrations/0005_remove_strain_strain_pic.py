# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfd_app', '0004_strain_strain_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strain',
            name='strain_pic',
        ),
    ]
