# Generated by Django 3.2 on 2022-02-05 02:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0018_assetstable_emaildate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetstable',
            name='emaildate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 2, 27, 55, 706051, tzinfo=utc)),
        ),
    ]
