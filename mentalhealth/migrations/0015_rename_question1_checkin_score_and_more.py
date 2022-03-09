# Generated by Django 4.0.2 on 2022-02-17 00:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mentalhealth', '0014_alter_entry_last_edit_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkin',
            old_name='question1',
            new_name='score',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question10',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question5',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question6',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question7',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question8',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='question9',
        ),
        migrations.AlterField(
            model_name='entry',
            name='last_edit_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 17, 0, 28, 18, 508235, tzinfo=utc)),
        ),
    ]