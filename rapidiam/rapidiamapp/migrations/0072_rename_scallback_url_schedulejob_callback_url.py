# Generated by Django 4.1.7 on 2023-06-19 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0071_remove_dataalertfieldfilter_callback_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulejob',
            old_name='scallback_url',
            new_name='callback_url',
        ),
    ]