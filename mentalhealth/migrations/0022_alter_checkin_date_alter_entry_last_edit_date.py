# Generated by Django 4.0.2 on 2022-02-17 01:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mentalhealth', '0021_alter_entry_last_edit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='date',
            field=models.DateField(default=datetime.date(2022, 2, 16)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='last_edit_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 17, 1, 49, 55, 497781, tzinfo=utc)),
        ),
    ]
