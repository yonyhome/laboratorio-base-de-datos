# Generated by Django 3.1.7 on 2021-04-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hijo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='padre',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
