# Generated by Django 2.0.3 on 2018-04-02 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('review_text_before', models.CharField(max_length=200)),
                ('review_text_after', models.CharField(max_length=200)),
                ('review_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Person')),
            ],
        ),
    ]
