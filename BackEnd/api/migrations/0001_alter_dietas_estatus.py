# Generated by Django 5.0.1 on 2024-04-18 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', 'triggers_nutricion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietas',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
    ]
