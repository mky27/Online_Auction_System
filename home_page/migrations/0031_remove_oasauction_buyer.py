# Generated by Django 5.0.3 on 2024-04-26 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0030_alter_oasauction_auction_created_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oasauction',
            name='buyer',
        ),
    ]
