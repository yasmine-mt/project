# Generated by Django 4.2.1 on 2023-06-01 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technicien', '0003_technicien_demandes_assignees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicien',
            name='demandes_assignees',
        ),
    ]
