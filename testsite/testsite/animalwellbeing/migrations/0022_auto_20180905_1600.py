# Generated by Django 2.1 on 2018-09-05 16:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animalwellbeing', '0021_auto_20180905_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coversheetformmodel',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 9, 5, 16, 0, 33, 715691)),
        ),
        migrations.AlterField(
            model_name='coversheetformmodel',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='animalwellbeing.Researchers'),
        ),
    ]