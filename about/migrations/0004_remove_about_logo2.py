# Generated by Django 5.0.1 on 2024-01-09 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_rename_logo_about_logo1_about_logo2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='logo2',
        ),
    ]