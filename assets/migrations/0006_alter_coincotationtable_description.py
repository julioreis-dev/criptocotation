# Generated by Django 3.2 on 2022-01-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20220126_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coincotationtable',
            name='description',
            field=models.CharField(max_length=150, verbose_name='Nome da criptomoeda'),
        ),
    ]
