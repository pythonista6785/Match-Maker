# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_useranswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 18, 10, 8, 22, 8360, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
