# Generated by Django 3.1.7 on 2021-04-02 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0002_auto_20210401_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hijo',
            name='hijode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gestion.padre'),
        ),
        migrations.AlterField(
            model_name='hijo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='padre',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
