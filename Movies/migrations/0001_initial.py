# Generated by Django 2.1.7 on 2019-04-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('imdb_id', models.CharField(max_length=9)),
            ],
        ),
    ]