from django.db import models


class ImagesInfo(models.Model):
    title = models.CharField('Title', max_length=60)
    year_link = models.CharField('Year', max_length=60)
    theme_link = models.CharField('Theme', max_length=60, blank=True)
    image_file = models.ImageField('File', upload_to='uploaded_images/')
    creation_date = models.DateField('Date of creation', blank=True)
    description = models.TextField('Description', blank=True)
