# Generated by Django 4.2 on 2023-05-09 11:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_amount_lamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount',
            name='lamp',
        ),
        migrations.AddField(
            model_name='amount',
            name='error',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), null=True, size=None),
        ),
    ]
