# Generated by Django 4.1.7 on 2023-02-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('medicinename', models.CharField(max_length=100)),
                ('medicinecategory', models.CharField(max_length=100)),
                ('symptoms', models.CharField(max_length=100)),
            ],
        ),
    ]