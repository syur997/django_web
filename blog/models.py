from django.db import models
import exifread as ef
from PIL import Image
from PIL.ExifTags import TAGS


# Create your models here.

class Fileupload(models.Model):
    title = models.CharField(max_length=200)
    imgfile = models.ImageField(null=True, upload_to='', blank=True)

    def __str__(self):
        return self.title


