# Generated by Django 3.2 on 2022-01-31 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0006_alter_coincotationtable_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetstable',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
    ]
