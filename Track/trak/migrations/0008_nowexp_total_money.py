# Generated by Django 4.2 on 2024-12-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0007_catfin_finance_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='nowexp',
            name='Total_money',
            field=models.BigIntegerField(default=0),
        ),
    ]