# Generated by Django 3.0.1 on 2019-12-30 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 16, 42, 46, 203203, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 16, 42, 46, 203172, tzinfo=utc)),
        ),
    ]