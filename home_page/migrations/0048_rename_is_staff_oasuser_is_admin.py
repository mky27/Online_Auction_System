# Generated by Django 5.0.3 on 2024-05-19 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0047_alter_oasauctionwinner_winner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oasuser',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
