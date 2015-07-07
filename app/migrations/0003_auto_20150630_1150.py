# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date created', blank=True),
        ),
    ]
