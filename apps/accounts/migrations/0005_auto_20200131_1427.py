# Generated by Django 3.0.1 on 2020-01-31 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_auto_20200131_1413'),
        ('accounts', '0004_auto_20200131_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university', to='universities.University'),
        ),
    ]
