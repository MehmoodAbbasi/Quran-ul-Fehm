# Generated by Django 5.1.4 on 2025-01-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunnah',
            name='description_ur',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sunnah',
            name='title_ar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
