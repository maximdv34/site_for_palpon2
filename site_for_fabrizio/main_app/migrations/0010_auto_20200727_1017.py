# Generated by Django 3.0.8 on 2020-07-27 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200721_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='info',
            new_name='name',
        ),
        migrations.AddField(
            model_name='client',
            name='text',
            field=models.TextField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]