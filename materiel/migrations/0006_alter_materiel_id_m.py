# Generated by Django 4.2.1 on 2023-05-29 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiel', '0005_rename_tag_materiel_departement_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='ID_M',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]