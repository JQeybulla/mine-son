# Generated by Django 3.1.3 on 2020-11-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_Media_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.TextField()),
                ('instagram', models.TextField()),
                ('youtube', models.TextField()),
                ('linkedin', models.TextField()),
            ],
        ),
    ]
