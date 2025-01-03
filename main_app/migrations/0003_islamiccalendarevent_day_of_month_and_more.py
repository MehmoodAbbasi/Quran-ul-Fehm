# Generated by Django 5.1.4 on 2025-01-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sunnah_description_ur_sunnah_title_ar'),
    ]

    operations = [
        migrations.AddField(
            model_name='islamiccalendarevent',
            name='day_of_month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='islamiccalendarevent',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='islamiccalendarevent',
            name='month_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='islamiccalendarevent',
            name='event_name',
            field=models.CharField(max_length=255),
        ),
    ]