# Generated by Django 4.2.4 on 2023-08-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
