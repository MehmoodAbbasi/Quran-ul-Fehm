# Generated by Django 5.1.4 on 2025-01-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_haddess'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='timezone',
            field=models.CharField(default='UTC', max_length=100),
        ),
    ]
