# Generated by Django 3.2 on 2022-05-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tupo_app', '0016_remove_community_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
