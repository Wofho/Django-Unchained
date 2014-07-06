# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='listuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='ListUser',
        ),
    ]
