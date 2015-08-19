# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150819_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='numberOfQuestions',
            new_name='NumberOfQuestions',
        ),
    ]
