# Generated by Django 3.2.2 on 2021-05-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_fdform_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cusignup',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
