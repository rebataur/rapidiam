# Generated by Django 4.1.7 on 2023-06-19 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0074_alter_schedulejob_last_run'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulejob',
            name='last_run',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]