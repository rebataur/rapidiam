# Generated by Django 4.1.6 on 2023-02-04 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0004_field_actual_name_field_entity_alter_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rapidiamapp.entity'),
        ),
    ]
