# Generated by Django 3.0.6 on 2020-05-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='min_text',
            field=models.CharField(max_length=1023, null=True),
        ),
    ]
