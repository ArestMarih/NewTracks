# Generated by Django 4.2 on 2024-12-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0006_persons_minlvl'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatFin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_F', models.TextField()),
                ('desc', models.TextField()),
                ('Income', models.BooleanField(default=None)),
                ('count', models.BigIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trak.catfin')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]