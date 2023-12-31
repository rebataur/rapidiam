# Generated by Django 4.1.7 on 2023-04-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0037_alter_field_actual_name_alter_field_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='functionmeta',
            name='function_code',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fieldfilter',
            name='filter_op',
            field=models.CharField(choices=[('EXACT', 'EXACT'), ('NOT', 'NOT'), ('LT', 'LESS THAN')], default='EXACT', max_length=30),
        ),
    ]
