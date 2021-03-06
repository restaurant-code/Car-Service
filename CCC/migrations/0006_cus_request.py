# Generated by Django 3.1.5 on 2021-02-04 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0005_auto_20210204_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='cus_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Four Wheeler with Gear', 'Four Wheeler with Gear'), ('Four Wheeler with Auto Gear', 'Four Wheeler with Auto Gear')], max_length=40)),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('brand', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('problem', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Repairing', 'Repairing'), ('Repairing Done', 'Repairing Done'), ('Released', 'Released')], default='Pending', max_length=40, null=True)),
                ('Customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CCC.customer')),
                ('Mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CCC.mechanic')),
            ],
        ),
    ]
