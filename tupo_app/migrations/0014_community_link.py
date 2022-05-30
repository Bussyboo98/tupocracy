# Generated by Django 3.2.13 on 2022-05-29 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tupo_app', '0013_community'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
