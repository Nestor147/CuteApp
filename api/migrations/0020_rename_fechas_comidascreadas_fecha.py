# Generated by Django 4.2.4 on 2023-10-23 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_rename_fecha_comidascreadas_fechas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comidascreadas',
            old_name='fechas',
            new_name='fecha',
        ),
    ]
