# Generated by Django 3.1.7 on 2021-04-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
