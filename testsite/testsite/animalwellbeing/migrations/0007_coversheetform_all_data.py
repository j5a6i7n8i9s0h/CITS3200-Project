# Generated by Django 2.1 on 2018-08-20 07:30

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('animalwellbeing', '0006_coversheetform_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='coversheetform',
            name='all_data',
            field=picklefield.fields.PickledObjectField(default=None, editable=False),
        ),
    ]
