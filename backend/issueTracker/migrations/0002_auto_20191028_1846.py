# Generated by Django 2.2.6 on 2019-10-28 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issueTracker', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AlterField(
            model_name='issues',
            name='activity',
            field=models.DateField(blank=True, null=True, verbose_name='last updated date'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='fixed_date',
            field=models.DateField(blank=True, null=True, verbose_name='date fixed'),
        ),
    ]
