# Generated by Django 2.1.1 on 2018-09-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kempo', '0006_auto_20180926_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='technique',
            name='category',
            field=models.CharField(choices=[('FORMS', 'Forms'), ('STRIKES', 'Strikes')], default='Uncategorized', max_length=20),
        ),
    ]
