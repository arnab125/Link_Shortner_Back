# Generated by Django 4.1.7 on 2023-03-24 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_url_custom_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='custom_url',
        ),
    ]
