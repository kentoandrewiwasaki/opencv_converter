# Generated by Django 2.2.6 on 2019-10-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0020_auto_20191016_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graymodel',
            name='gray_image',
            field=models.ImageField(default='output/gray/gray.jpg', upload_to='output/gray'),
        ),
    ]