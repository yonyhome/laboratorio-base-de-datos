# Generated by Django 3.1.7 on 2021-04-01 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('hijode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.padre')),
            ],
        ),
    ]
