# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20150928_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='notes_category',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
