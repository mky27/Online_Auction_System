# Generated by Django 5.0.3 on 2024-04-23 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0029_alter_oasauction_auction_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oasauction',
            name='auction_created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
