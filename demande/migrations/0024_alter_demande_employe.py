# Generated by Django 4.2.1 on 2023-06-23 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0004_alter_employe_id_e'),
        ('demande', '0023_alter_demande_employe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='employe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employe.employe'),
        ),
    ]