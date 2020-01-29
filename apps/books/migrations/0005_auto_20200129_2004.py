# Generated by Django 3.0.1 on 2020-01-29 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200129_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 20, 4, 30, 726779, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 20, 4, 30, 726804, tzinfo=utc)),
        ),
    ]
