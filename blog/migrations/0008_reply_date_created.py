# Generated by Django 3.0.6 on 2020-05-28 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
