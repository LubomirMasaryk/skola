# Generated by Django 5.1.1 on 2025-01-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meno', models.CharField(max_length=20)),
                ('priezvisko', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kniha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=20)),
                ('rok_vydania', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Kniha',
                'verbose_name_plural': 'Knihy',
                'ordering': ['nazov'],
            },
        ),
        migrations.CreateModel(
            name='Miesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vydavatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazov', models.CharField(max_length=50)),
            ],
        ),
    ]
