# Generated by Django 3.0.5 on 2021-02-06 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0009_auto_20210206_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='fname',
            new_name='name',
        ),
    ]
