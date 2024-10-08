# Generated by Django 4.2.11 on 2024-06-02 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelands', '0005_delete_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_games', models.IntegerField()),
                ('game_name', models.CharField(max_length=100)),
                ('release_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2026)])),
                ('metacritic_score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('developers', models.CharField(blank=True, max_length=100, null=True)),
                ('howlongtobeat', models.IntegerField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
