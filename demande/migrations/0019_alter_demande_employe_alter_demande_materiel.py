# Generated by Django 4.2.1 on 2023-06-01 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0004_alter_employe_id_e'),
        ('materiel', '0009_remove_materiel_nom_m_remove_materiel_qte_enstock'),
        ('demande', '0018_remove_demande_demandes_assignees_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='employe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employe.employe'),
        ),
        migrations.AlterField(
            model_name='demande',
            name='materiel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='materiel.materiel', unique=True),
        ),
    ]
