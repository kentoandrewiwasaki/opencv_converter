# Generated by Django 2.2.6 on 2019-10-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0014_auto_20191014_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animemodel',
            name='anime_image',
            field=models.ImageField(default='output/anime/anime.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='animemodel',
            name='image',
            field=models.ImageField(upload_to='input/anime'),
        ),
        migrations.AlterField(
            model_name='facemosaicmodel',
            name='facemosaic_image',
            field=models.ImageField(default='output/facemosaic/facemosaic.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='facemosaicmodel',
            name='image',
            field=models.ImageField(upload_to='input/facemosaic'),
        ),
        migrations.AlterField(
            model_name='facereadmodel',
            name='faceread_image',
            field=models.ImageField(default='output/faceread/faceread.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='facereadmodel',
            name='image',
            field=models.ImageField(upload_to='input/faceread'),
        ),
        migrations.AlterField(
            model_name='graymodel',
            name='gray_image',
            field=models.ImageField(default='output/gray/gray.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='graymodel',
            name='image',
            field=models.ImageField(upload_to='input/gray'),
        ),
        migrations.AlterField(
            model_name='mosaicmodel',
            name='image',
            field=models.ImageField(upload_to='input/mosaic'),
        ),
        migrations.AlterField(
            model_name='mosaicmodel',
            name='mosaic_image',
            field=models.ImageField(default='output/mosaic/mosaic.jpg', upload_to=''),
        ),
    ]
