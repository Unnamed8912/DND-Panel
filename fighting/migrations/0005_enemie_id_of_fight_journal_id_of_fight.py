# Generated by Django 5.1.4 on 2025-01-17 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighting', '0004_fight'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemie',
            name='id_of_fight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fighting.fight'),
        ),
        migrations.AddField(
            model_name='journal',
            name='id_of_fight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fighting.fight'),
        ),
    ]
