# Generated by Django 3.2.2 on 2021-05-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_auto_20210514_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuitems',
            name='clothprice',
            field=models.DecimalField(blank=True, decimal_places=10, default=None, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='fdform',
            name='clothprice',
            field=models.DecimalField(blank=True, decimal_places=10, default=None, max_digits=20, null=True),
        ),
    ]
