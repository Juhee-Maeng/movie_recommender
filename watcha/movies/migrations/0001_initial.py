# Generated by Django 3.0.6 on 2020-08-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('img_link', models.CharField(max_length=100)),
                ('pubYear', models.IntegerField()),
                ('userRating', models.FloatField()),
                ('director', models.CharField(max_length=50)),
                ('actor', models.TextField()),
                ('summary', models.TextField()),
                ('nation', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'movie_information',
            },
        ),
    ]
