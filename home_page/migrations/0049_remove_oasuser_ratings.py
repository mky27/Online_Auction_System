# Generated by Django 5.0.3 on 2024-05-19 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0048_rename_is_staff_oasuser_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oasuser',
            name='ratings',
        ),
    ]
