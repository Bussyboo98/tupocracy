# Generated by Django 3.2.13 on 2022-05-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tupo_app', '0005_auto_20220514_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='birthday',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]