

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
