# Generated by Django 3.1.6 on 2021-04-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_auto_20210405_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.IntegerField(),
        ),
    ]