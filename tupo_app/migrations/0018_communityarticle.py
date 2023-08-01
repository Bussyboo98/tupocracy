# Generated by Django 3.2.3 on 2023-08-01 14:16

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tupo_app', '0017_community_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Community Article',
            },
        ),
    ]
