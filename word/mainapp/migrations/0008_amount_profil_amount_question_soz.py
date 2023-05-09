# Generated by Django 4.2 on 2023-05-09 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('mainapp', '0007_amount_acceptance_amount_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='amount',
            name='profil',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userapp.profil'),
        ),
        migrations.AddField(
            model_name='amount',
            name='question_soz',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
