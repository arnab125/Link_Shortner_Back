# Generated by Django 4.1.6 on 2023-03-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('short_url', models.CharField(default='AR4LP', max_length=1000)),
            ],
        ),
    ]
