# Generated by Django 3.1.3 on 2020-11-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='faculty_text',
            field=models.TextField(default='Faculty'),
        ),
    ]
