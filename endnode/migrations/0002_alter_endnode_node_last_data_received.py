# Generated by Django 3.2.3 on 2021-05-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endnode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endnode',
            name='node_last_data_received',
            field=models.DateTimeField(choices=[('active', 'Aktif'), ('passive', 'Pasif')], max_length=10),
        ),
    ]
