# Generated by Django 2.2.6 on 2019-11-03 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issueTracker', '0008_auto_20191103_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 3, 18, 23, 24, 551141), verbose_name='date created'),
        ),
    ]
