# Generated by Django 4.1.6 on 2023-03-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
