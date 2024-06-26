# Generated by Django 5.0.1 on 2024-01-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landing',
            name='description',
        ),
        migrations.RemoveField(
            model_name='landing',
            name='image',
        ),
        migrations.RemoveField(
            model_name='landing',
            name='title',
        ),
        migrations.AddField(
            model_name='landing',
            name='description_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landing',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='landing',
            name='image_ar',
            field=models.ImageField(blank=True, null=True, upload_to='landing_images/'),
        ),
        migrations.AddField(
            model_name='landing',
            name='image_en',
            field=models.ImageField(blank=True, null=True, upload_to='landing_images/'),
        ),
        migrations.AddField(
            model_name='landing',
            name='title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='landing',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
