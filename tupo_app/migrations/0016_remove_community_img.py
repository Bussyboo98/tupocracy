# Generated by Django 3.2 on 2022-05-30 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tupo_app', '0015_community_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='img',
        ),
    ]
