# Generated by Django 3.2 on 2022-01-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20220120_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coincotationtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.IntegerField(verbose_name='Noma da criptomoeda')),
                ('price', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Cotações',
                'verbose_name_plural': 'Cotação',
            },
        ),
        migrations.AlterField(
            model_name='assetstable',
            name='timer',
            field=models.IntegerField(choices=[(5, '5'), (10, '10'), (20, '20'), (30, '30'), (60, '60')], default=30, help_text='(mins)', verbose_name='Timer de alerta'),
        ),
    ]
