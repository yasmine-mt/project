# Generated by Django 4.2.1 on 2023-05-31 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0006_alter_demande_id_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='statuts',
            field=models.CharField(choices=[(' traitée', ' traitée'), ('en cours', 'en cours'), ('non traitée ', 'non traitée')], max_length=200, null=True),
        ),
    ]