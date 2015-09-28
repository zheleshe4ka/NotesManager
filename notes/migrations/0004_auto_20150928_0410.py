# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20150926_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_notes',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
