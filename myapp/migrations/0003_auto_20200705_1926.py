# Generated by Django 3.0.8 on 2020-07-05 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200705_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='sale',
            new_name='sold',
        ),
    ]
