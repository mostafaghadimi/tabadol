# Generated by Django 3.0.1 on 2020-01-31 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20200131_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 14, 25, 42, 524542, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 14, 25, 42, 524567, tzinfo=utc)),
        ),
    ]