# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='result',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bet',
            name='title',
            field=models.CharField(max_length=50, default='Bet'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='engine_id',
            field=models.IntegerField(null=True),
        ),
    ]
