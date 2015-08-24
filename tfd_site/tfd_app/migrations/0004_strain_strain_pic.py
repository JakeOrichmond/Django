# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfd_app', '0003_auto_20150731_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='strain_pic',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
