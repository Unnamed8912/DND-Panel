# Generated by Django 5.1.4 on 2025-01-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('level', models.IntegerField(default=1)),
                ('klass', models.CharField(max_length=50)),
                ('rasa', models.CharField(max_length=50)),
                ('max_health', models.PositiveIntegerField(default=10)),
                ('cur_health', models.IntegerField(default=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='character_images')),
            ],
            options={
                'verbose_name': 'Персонажа',
                'verbose_name_plural': 'Персонажи',
                'db_table': 'character',
            },
        ),
    ]
