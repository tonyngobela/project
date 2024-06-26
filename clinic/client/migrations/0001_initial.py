# Generated by Django 5.0.4 on 2024-06-24 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Docteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('sexe', models.CharField(max_length=1)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.service')),
            ],
        ),
    ]
