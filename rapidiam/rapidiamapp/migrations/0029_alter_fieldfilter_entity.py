# Generated by Django 4.1.6 on 2023-02-18 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0028_rename_field_col_fieldfilter_filter_col'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldfilter',
            name='entity',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rapidiamapp.entity'),
            preserve_default=False,
        ),
    ]