# Generated by Django 5.0.1 on 2024-01-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='url',
        ),
        migrations.AddField(
            model_name='footer',
            name='url1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='url2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='url3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='url4',
            field=models.URLField(blank=True, null=True),
        ),
    ]