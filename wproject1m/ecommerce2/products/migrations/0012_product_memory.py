# Generated by Django 2.0 on 2018-10-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='memory',
            field=models.TextField(default=2),
        ),
    ]
