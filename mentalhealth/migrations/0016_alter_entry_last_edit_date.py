# Generated by Django 4.0.2 on 2022-02-17 00:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mentalhealth', '0015_rename_question1_checkin_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='last_edit_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
