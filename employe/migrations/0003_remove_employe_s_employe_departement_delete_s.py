# Generated by Django 4.2.1 on 2023-05-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0002_s_remove_employe_departement_employe_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='s',
        ),
        migrations.AddField(
            model_name='employe',
            name='departement',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='s',
        ),
    ]
