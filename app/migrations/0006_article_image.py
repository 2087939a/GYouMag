# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'', storage=django.core.files.storage.FileSystemStorage(location=b'/media/'), upload_to=b''),
        ),
    ]
