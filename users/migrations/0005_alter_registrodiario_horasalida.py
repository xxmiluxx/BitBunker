# Generated by Django 5.1.1 on 2024-11-18 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_registrodiario_horasalida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrodiario',
            name='horaSalida',
            field=models.DateTimeField(null=True),
        ),
    ]
