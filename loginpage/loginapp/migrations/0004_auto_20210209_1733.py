# Generated by Django 3.1.6 on 2021-02-09 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_delete_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AlterModelTable(
            name='member',
            table='loginapp_member',
        ),
    ]
