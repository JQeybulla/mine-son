# Generated by Django 3.1.3 on 2020-11-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_greeting_about_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeting',
            name='about_club',
            field=models.TextField(default='This is club'),
        ),
        migrations.AddField(
            model_name='greeting',
            name='about_students',
            field=models.TextField(default='This is students'),
        ),
        migrations.AddField(
            model_name='greeting',
            name='about_teachers',
            field=models.TextField(default='This is techhers'),
        ),
    ]
