# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfd_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='strain_info',
            field=models.CharField(default='', max_length=1080),
            preserve_default=False,
        ),
    ]
