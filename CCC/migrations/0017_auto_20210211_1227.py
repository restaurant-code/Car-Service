# Generated by Django 3.1.5 on 2021-02-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0016_auto_20210211_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_leave',
            name='admin_reason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]