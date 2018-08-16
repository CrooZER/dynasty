# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180710_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='first_side_bet',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='second_side_bet',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='result',
            field=models.IntegerField(null=True),
        ),
    ]
