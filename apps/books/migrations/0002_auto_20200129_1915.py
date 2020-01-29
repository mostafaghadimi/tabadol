# Generated by Django 3.0.1 on 2020-01-29 19:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 19, 15, 53, 774588, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 19, 15, 53, 774615, tzinfo=utc)),
        ),
    ]