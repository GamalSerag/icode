# Generated by Django 5.0.1 on 2024-01-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_description_ar_service_title_ar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='./static/service/images/'),
        ),
    ]
