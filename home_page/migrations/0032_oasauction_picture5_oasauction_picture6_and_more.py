# Generated by Django 5.0.3 on 2024-04-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0031_remove_oasauction_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='oasauction',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='auction_pictures/'),
        ),
        migrations.AddField(
            model_name='oasauction',
            name='picture6',
            field=models.ImageField(blank=True, null=True, upload_to='auction_pictures/'),
        ),
        migrations.AddField(
            model_name='oasauction',
            name='picture7',
            field=models.ImageField(blank=True, null=True, upload_to='auction_pictures/'),
        ),
        migrations.AlterField(
            model_name='oasauction',
            name='item_cat',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='oasauction',
            name='picture1',
            field=models.ImageField(upload_to='auction_pictures/'),
        ),
        migrations.AlterField(
            model_name='oasauction',
            name='picture2',
            field=models.ImageField(upload_to='auction_pictures/'),
        ),
        migrations.AlterField(
            model_name='oasauction',
            name='picture3',
            field=models.ImageField(upload_to='auction_pictures/'),
        ),
        migrations.AlterField(
            model_name='oasauction',
            name='picture4',
            field=models.ImageField(upload_to='auction_pictures/'),
        ),
    ]