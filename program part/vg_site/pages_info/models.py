from django.db import models


class PageInfo(models.Model):
    title = models.CharField('Title', max_length=60)
    nav_title = models.CharField('Navigation Title', max_length=60)
    main_page_dialog = models.CharField('Dialog Title', max_length=60, blank=True)
    permalink = models.CharField('Permalink', max_length=20, unique=True)
    update_date = models.DateTimeField('Last Updated')
    main_text = models.TextField('Main Text', blank=True)

    def __str__(self):
        return self.nav_title
