# Generated by Django 5.0.3 on 2024-04-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0021_alter_oasauction_picture1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oasauction',
            name='auction_created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
