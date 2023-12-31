# Generated by Django 4.1.6 on 2023-02-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0018_functionmeta_return_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='derived_type',
        ),
        migrations.RemoveField(
            model_name='field',
            name='is_derived_column',
        ),
        migrations.AlterField(
            model_name='argumentmeta',
            name='type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('INTEGER', 'Integer'), ('NUMERIC', 'Numeric'), ('DATE', 'Date'), ('BINARY', 'Binary'), ('COLUMN', 'Column'), ('DERIVED', 'Derived')], default='TEXT', max_length=20),
        ),
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('INTEGER', 'Integer'), ('NUMERIC', 'Numeric'), ('DATE', 'Date'), ('BINARY', 'Binary'), ('COLUMN', 'Column'), ('DERIVED', 'Derived')], default='TEXT', max_length=20),
        ),
        migrations.AlterField(
            model_name='functionmeta',
            name='return_type',
            field=models.CharField(choices=[('TEXT', 'Text'), ('INTEGER', 'Integer'), ('NUMERIC', 'Numeric'), ('DATE', 'Date'), ('BINARY', 'Binary'), ('COLUMN', 'Column'), ('DERIVED', 'Derived')], default='TEXT', max_length=20),
        ),
    ]
