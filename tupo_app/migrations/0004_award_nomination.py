# Generated by Django 3.2.13 on 2022-05-14 15:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tupo_app', '0003_alter_aboutusmodel_about_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Award',
            },
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Yes', 'Yes'), ('No', ' No'), ('', 'Select')], default='', max_length=40)),
                ('drop_time', models.CharField(max_length=200, verbose_name='Date/Time')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=200, verbose_name='Date/Time')),
                ('employer', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('home', models.CharField(max_length=200, verbose_name='Home Address')),
                ('email', models.CharField(max_length=40)),
                ('select_all', models.CharField(choices=[('Dr.', 'Dr.'), ('Doctor', ' Doctor'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('', 'Choose Title')], default='', max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Award',
            },
        ),
    ]
