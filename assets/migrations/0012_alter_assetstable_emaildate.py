# Generated by Django 3.2 on 2022-02-03 21:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_alter_assetstable_emaildate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetstable',
            name='emaildate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
