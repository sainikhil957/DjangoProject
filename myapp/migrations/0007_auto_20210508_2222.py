# Generated by Django 3.2.2 on 2021-05-08 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_fdmodels_clothfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fdmodels',
            new_name='Fdmodel',
        ),
        migrations.AlterModelTable(
            name='fdmodel',
            table='fdmodel_table',
        ),
    ]
