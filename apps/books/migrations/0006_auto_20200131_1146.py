# Generated by Django 3.0.1 on 2020-01-31 11:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200129_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 11, 46, 26, 910968, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 11, 46, 26, 910993, tzinfo=utc)),
        ),
    ]
