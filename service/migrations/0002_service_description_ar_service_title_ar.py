# Generated by Django 5.0.1 on 2024-01-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
