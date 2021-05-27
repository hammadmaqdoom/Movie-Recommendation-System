# Generated by Django 3.2.3 on 2021-05-27 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userMovieWatched',
            fields=[
                ('movieNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('movieWatched', models.CharField(max_length=200)),
                ('movieRating', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
