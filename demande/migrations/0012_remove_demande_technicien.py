# Generated by Django 4.2.1 on 2023-06-01 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0011_demande_technicien'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='technicien',
        ),
    ]