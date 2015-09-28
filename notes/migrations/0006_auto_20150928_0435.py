# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_notes_notes_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='notes_uuid',
        ),
        migrations.AddField(
            model_name='notes',
            name='notes_favorite',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
