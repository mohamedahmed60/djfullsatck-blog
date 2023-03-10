# Generated by Django 4.1.4 on 2023-01-06 23:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=10000000),
        ),
    ]
