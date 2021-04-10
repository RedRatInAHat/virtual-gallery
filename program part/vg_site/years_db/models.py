from django.db import models


class YearsInfo(models.Model):
    title = models.CharField('Title', max_length=60)
    permalink = models.CharField('Permalink', max_length=20, unique=True)
    main_text = models.TextField('Main Text', blank=True)
    update_date = models.DateTimeField('Last Updated', auto_now=True)
