# Generated by Django 2.0.3 on 2018-04-03 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20180403_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Комментатор', 'verbose_name_plural': 'Комментаторы'},
        ),
    ]
