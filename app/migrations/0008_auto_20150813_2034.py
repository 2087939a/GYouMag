# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150813_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default=b'', upload_to=b'', width_field=b'width', storage=django.core.files.storage.FileSystemStorage(location=b'/media/'), height_field=b'height'),
        ),
    ]
