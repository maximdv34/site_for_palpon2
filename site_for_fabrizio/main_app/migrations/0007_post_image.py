# Generated by Django 3.0.4 on 2020-07-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200703_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]