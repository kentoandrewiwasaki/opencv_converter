from django.db import models
from cloudinary.models import CloudinaryField

class GrayModel(models.Model):
    image = CloudinaryField(upload_to="input/gray")
    gray_image = CloudinaryField(default = 'output/gray/gray.jpg')

class FaceReadModel(models.Model):
    image = CloudinaryField(upload_to="input/faceread")
    faceread_image = CloudinaryField(default = 'output/faceread/faceread.jpg')

class AnimeModel(models.Model):
    image = CloudinaryField(upload_to="input/anime")
    anime_image = CloudinaryField(default = 'output/anime/anime.jpg')

class MosaicModel(models.Model):
    image = CloudinaryField(upload_to="input/mosaic")
    mosaic_image = CloudinaryField(default = 'output/mosaic/mosaic.jpg')

class FaceMosaicModel(models.Model):
    image = CloudinaryField(upload_to="input/facemosaic")
    facemosaic_image = CloudinaryField(default = 'output/facemosaic/facemosaic.jpg')