# Generated by Django 5.0.1 on 2024-05-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('accno', models.CharField(max_length=100)),
                ('cust_state', models.CharField(max_length=100)),
                ('cust_pin', models.CharField(max_length=100)),
                ('dpd', models.IntegerField()),
            ],
        ),
    ]