# Generated by Django 4.1.7 on 2023-06-15 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidiamapp', '0062_alter_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitychildren',
            name='child_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_entity', to='rapidiamapp.entity'),
        ),
        migrations.AlterField(
            model_name='entitychildren',
            name='child_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_field', to='rapidiamapp.field'),
        ),
        migrations.AlterField(
            model_name='entitychildren',
            name='parent_entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_entity', to='rapidiamapp.entity'),
        ),
        migrations.AlterField(
            model_name='entitychildren',
            name='parent_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_field', to='rapidiamapp.field'),
        ),
    ]