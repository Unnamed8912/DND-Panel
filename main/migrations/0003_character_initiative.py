# Generated by Django 5.1.4 on 2025-01-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_character_cur_health_alter_character_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='initiative',
            field=models.IntegerField(default=0),
        ),
    ]
