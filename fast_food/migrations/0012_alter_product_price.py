# Generated by Django 4.1.1 on 2022-12-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_food', '0011_rename_picture_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
