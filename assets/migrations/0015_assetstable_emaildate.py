# Generated by Django 3.2 on 2022-02-04 01:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0014_remove_assetstable_emaildate'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetstable',
            name='emaildate',
            field=models.DateField(default=datetime.datetime(2022, 2, 3, 22, 13, 54, 717505)),
        ),
    ]
