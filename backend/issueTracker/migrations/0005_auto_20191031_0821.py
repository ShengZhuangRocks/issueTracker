# Generated by Django 2.2.6 on 2019-10-30 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issueTracker', '0004_auto_20191031_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='priority',
            field=models.CharField(choices=[('1', 'Highest'), ('2', 'High'), ('3', 'Medium'), ('4', 'Lower'), ('5', 'Lowest'), ('6', 'Done')], max_length=2),
        ),
    ]
