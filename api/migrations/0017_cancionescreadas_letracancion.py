# Generated by Django 4.2.4 on 2023-09-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_usuario_mensaje_diario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancionescreadas',
            name='letraCancion',
            field=models.TextField(default=''),
        ),
    ]
