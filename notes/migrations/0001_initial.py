# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes_title', models.TextField()),
                ('notes_text', models.TextField()),
                ('notes_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'notes',
            },
        ),
    ]
