# Generated by Django 2.1.1 on 2018-09-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kempo', '0004_auto_20180925_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
