# Generated by Django 3.0.1 on 2020-01-29 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200129_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 20, 2, 12, 764926, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 20, 2, 12, 764952, tzinfo=utc)),
        ),
    ]
