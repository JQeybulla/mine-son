# Generated by Django 3.1.3 on 2020-11-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201109_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='about_department',
            field=models.TextField(blank=True, default='Nome', null=True),
        ),
    ]
