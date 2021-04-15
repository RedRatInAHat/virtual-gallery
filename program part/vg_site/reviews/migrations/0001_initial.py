# Generated by Django 3.1.7 on 2021-04-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_type', models.CharField(choices=[('suggestion', 'suggestion'), ('review', 'review')], max_length=10, verbose_name='Review Type: ')),
                ('review_text', models.TextField(verbose_name='Text: ')),
                ('name', models.CharField(default='Unknown', max_length=60, verbose_name='From: ')),
            ],
        ),
    ]
