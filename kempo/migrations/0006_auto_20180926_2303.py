# Generated by Django 2.1.1 on 2018-09-27 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kempo', '0005_auto_20180925_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='notes',
            field=models.TextField(),
        ),
    ]
