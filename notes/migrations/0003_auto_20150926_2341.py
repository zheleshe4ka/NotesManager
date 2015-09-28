# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes_title',
            field=models.CharField(max_length=100),
        ),
    ]
