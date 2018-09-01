# Generated by Django 2.1 on 2018-08-20 07:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animalwellbeing', '0011_coversheetform_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='coversheetform',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='coversheetform',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 8, 20, 7, 41, 49, 665999)),
        ),
        migrations.AlterField(
            model_name='coversheetform',
            name='creator',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to='animalwellbeing.Researchers'),
        ),
    ]
