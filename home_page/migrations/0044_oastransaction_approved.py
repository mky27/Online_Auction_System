# Generated by Django 5.0.3 on 2024-05-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0043_oasuser_balance_oastransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='oastransaction',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
