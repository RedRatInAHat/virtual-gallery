# Generated by Django 3.1.7 on 2021-04-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('year_link', models.CharField(max_length=60, verbose_name='Year')),
                ('theme_link', models.CharField(blank=True, max_length=60, verbose_name='Theme')),
                ('image_file', models.FileField(upload_to='uploaded_images/', verbose_name='File')),
                ('creation_date', models.DateTimeField(blank=True, verbose_name='Date of creation')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
    ]
