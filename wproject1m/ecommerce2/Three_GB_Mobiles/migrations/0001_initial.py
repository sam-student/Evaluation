# Generated by Django 2.0 on 2019-02-07 17:51

import Three_GB_Mobiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Three_GB_Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=39.99, max_digits=20)),
                ('Charging', models.TextField(default='good speakers')),
                ('Torch', models.TextField(default='2GB')),
                ('Games', models.TextField(default='8MP')),
                ('Messaging', models.TextField(default='None')),
                ('Browser', models.TextField(default='None')),
                ('Audio', models.TextField(default='None')),
                ('Data', models.TextField(default='None')),
                ('NFC', models.TextField(default='None')),
                ('USB', models.TextField(default='None')),
                ('GPS', models.TextField(default='None')),
                ('Bluetooth', models.TextField(default='None')),
                ('Wifi', models.TextField(default='None')),
                ('Front', models.TextField(default='None')),
                ('Main', models.TextField(default='None')),
                ('card', models.TextField(default='None')),
                ('BuiltIn', models.TextField(default='None')),
                ('Features', models.TextField(default='None')),
                ('Protection', models.TextField(default='None')),
                ('Resolution', models.TextField(default='None')),
                ('Size', models.TextField(default='None')),
                ('Technology', models.TextField(default='None')),
                ('GPU', models.TextField(default='None')),
                ('Chipset', models.TextField(default='None')),
                ('CPU', models.TextField(default='None')),
                ('FourGBand', models.TextField(default='None')),
                ('ThreeGBand', models.TextField(default='None')),
                ('TwoGBand', models.TextField(default='None')),
                ('Color', models.TextField(default='None')),
                ('SIM', models.TextField(default='None')),
                ('Weight', models.TextField(default='None')),
                ('Dimension', models.TextField(default='None')),
                ('UIBuild', models.TextField(default='None')),
                ('OperatingSystem', models.TextField(default='None')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Three_GB_Mobiles.models.upload_image_path)),
                ('image1', models.ImageField(blank=True, null=True, upload_to=Three_GB_Mobiles.models.upload_image_path)),
                ('image2', models.ImageField(blank=True, null=True, upload_to=Three_GB_Mobiles.models.upload_image_path)),
                ('Review_count', models.TextField(default='None')),
                ('Average_Rating', models.TextField(default='None')),
                ('Reviews', models.TextField(default='None')),
                ('Ram', models.TextField(default='None')),
            ],
        ),
    ]
