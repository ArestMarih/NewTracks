# Generated by Django 4.2 on 2024-12-04 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0009_rename_name_f_finance_name_f'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finance',
            old_name='name_f',
            new_name='nameF',
        ),
    ]
