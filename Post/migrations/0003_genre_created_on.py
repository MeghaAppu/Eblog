# Generated by Django 2.2.11 on 2021-06-03 08:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20210601_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]