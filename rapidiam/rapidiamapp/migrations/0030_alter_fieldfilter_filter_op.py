# Generated by Django 4.1.6 on 2023-02-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0029_alter_fieldfilter_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldfilter',
            name='filter_op',
            field=models.CharField(max_length=30),
        ),
    ]
