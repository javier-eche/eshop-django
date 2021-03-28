from django.db import models


class Subcategory(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)


class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    subcategories = models.ManyToManyField(Subcategory)



def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)