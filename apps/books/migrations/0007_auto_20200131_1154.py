# Generated by Django 3.0.1 on 2020-01-31 11:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200131_1146'),
        ('books', '0006_auto_20200131_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 11, 54, 50, 383430, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 11, 54, 50, 383709, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='books',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.Profile'),
        ),
    ]
