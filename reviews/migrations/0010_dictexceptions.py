# Generated by Django 2.0.3 on 2018-04-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_dictcurse'),
    ]

    operations = [
        migrations.CreateModel(
            name='DictExceptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=15)),
            ],
        ),
    ]
