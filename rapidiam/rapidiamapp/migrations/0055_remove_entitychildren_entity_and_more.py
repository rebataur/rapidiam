# Generated by Django 4.1.7 on 2023-06-15 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0054_entitychildren'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entitychildren',
            name='entity',
        ),
        migrations.AddField(
            model_name='entitychildren',
            name='parent_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rapidiamapp.entity'),
        ),
    ]