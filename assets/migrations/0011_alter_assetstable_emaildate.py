# Generated by Django 3.2 on 2022-02-03 21:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_alter_assetstable_emaildate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetstable',
            name='emaildate',
            field=models.DateField(default=datetime.datetime(2022, 2, 3, 21, 50, 52, 672494, tzinfo=utc)),
        ),
    ]
