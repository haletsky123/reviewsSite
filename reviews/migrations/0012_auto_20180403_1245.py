# Generated by Django 2.0.3 on 2018-04-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20180403_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(editable=False, verbose_name='date published'),
        ),
    ]