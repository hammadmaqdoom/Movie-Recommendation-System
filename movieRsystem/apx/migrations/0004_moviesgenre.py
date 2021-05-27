# Generated by Django 3.2.3 on 2021-05-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apx', '0003_moviesdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='moviesgenre',
            fields=[
                ('movieId', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('imdbID', models.IntegerField()),
                ('year', models.IntegerField()),
                ('rtPictureURL', models.URLField()),
            ],
        ),
    ]