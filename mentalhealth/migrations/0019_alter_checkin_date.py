# Generated by Django 4.0.2 on 2022-02-17 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalhealth', '0018_alter_checkin_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='date',
            field=models.DateTimeField(default=datetime.date(2022, 2, 17)),
        ),
    ]
