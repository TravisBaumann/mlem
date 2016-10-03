# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_posting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterposts',
            name='date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime.now),
        ),
    ]
