# Generated by Django 4.2.16 on 2024-12-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MODELS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('Gmail', models.CharField(max_length=200)),
            ],
        ),
    ]
