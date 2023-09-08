# Generated by Django 4.2.1 on 2023-05-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='s',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departement', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employe',
            name='departement',
        ),
        migrations.AddField(
            model_name='employe',
            name='s',
            field=models.ManyToManyField(to='employe.s'),
        ),
    ]
