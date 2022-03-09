# Generated by Django 4.0.2 on 2022-02-15 03:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentalhealth', '0010_alter_entry_options_alter_entry_last_edit_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.IntegerField()),
                ('question2', models.IntegerField()),
                ('question3', models.IntegerField()),
                ('question4', models.IntegerField()),
                ('question5', models.IntegerField()),
                ('question6', models.IntegerField()),
                ('question7', models.IntegerField()),
                ('question8', models.IntegerField()),
                ('question9', models.IntegerField()),
                ('question10', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
