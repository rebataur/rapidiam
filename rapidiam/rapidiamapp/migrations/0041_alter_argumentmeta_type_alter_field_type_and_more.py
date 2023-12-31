# Generated by Django 4.2 on 2023-05-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0040_remove_field_is_calculated_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='argumentmeta',
            name='type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('INTEGER', 'Integer'), ('NUMERIC', 'Numeric'), ('DATE', 'Date'), ('BINARY', 'Binary'), ('PNG_IMAGE', 'PNG Image'), ('COLUMN', 'Column')], default='TEXT', max_length=20),
        ),
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('INTEGER', 'Integer'), ('NUMERIC', 'Numeric'), ('DATE', 'Date'), ('BINARY', 'Binary'), ('PNG_IMAGE', 'PNG Image'), ('COLUMN', 'Column')], default='TEXT', max_length=64),
        ),
        migrations.AlterField(
            model_name='functionmeta',
            name='return_type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('INTEGER', 'Integer'), ('NUMERIC', 'Numeric'), ('DATE', 'Date'), ('BINARY', 'Binary'), ('PNG_IMAGE', 'PNG Image'), ('COLUMN', 'Column')], default='TEXT', max_length=20),
        ),
        migrations.AlterField(
            model_name='functionmeta',
            name='type',
            field=models.CharField(choices=[('CALCULATION', 'Calculation'), ('VISUALIZE', 'Visualize'), ('DATASCIENCE', 'DataScience'), ('DERIVED', 'Derived')], default='CALCULATION', max_length=20),
        ),
    ]
