# Generated by Django 3.0.4 on 2020-06-16 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
