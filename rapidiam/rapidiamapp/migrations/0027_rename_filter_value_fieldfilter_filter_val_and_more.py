# Generated by Django 4.1.6 on 2023-02-17 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0026_remove_fieldfilter_field_fieldfilter_field_col_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fieldfilter',
            old_name='filter_value',
            new_name='filter_val',
        ),
        migrations.AddField(
            model_name='fieldfilter',
            name='entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rapidiamapp.entity'),
        ),
    ]
