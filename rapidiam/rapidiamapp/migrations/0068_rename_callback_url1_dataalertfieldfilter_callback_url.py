# Generated by Django 4.1.7 on 2023-06-19 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0067_rename_callback_url_dataalertfieldfilter_callback_url1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataalertfieldfilter',
            old_name='callback_url1',
            new_name='callback_url',
        ),
    ]
