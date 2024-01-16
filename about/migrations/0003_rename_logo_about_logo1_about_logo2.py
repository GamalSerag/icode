# Generated by Django 5.0.1 on 2024-01-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='logo',
            new_name='logo1',
        ),
        migrations.AddField(
            model_name='about',
            name='logo2',
            field=models.ImageField(null=True, upload_to='images/logo'),
        ),
    ]