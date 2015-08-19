# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150819_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='QuestionType',
            field=models.CharField(max_length=25),
        ),
    ]
