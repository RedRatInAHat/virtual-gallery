from django.db import models


class YearsInfo(models.Model):
    title = models.CharField('Title', max_length=60)
    permalink = models.CharField('Permalink', max_length=20, unique=True)
    main_text = models.TextField('Main Text', blank=True)
    update_date = models.DateTimeField('Last Updated', auto_now=True)


class ThemesInfo(models.Model):
    year_choices = {(year.title, year.permalink[1:-1]) for year in
                    YearsInfo.objects.all().order_by('permalink')}
    title = models.CharField('Title', max_length=60)
    nav_title = models.CharField('Navigation Title', max_length=60)
    permalink = models.CharField('Permalink', max_length=20)
    year = models.CharField("Year Title", max_length=60, choices=year_choices)
    main_text = models.TextField('Main Text', blank=True)
    update_date = models.DateTimeField('Last Updated', auto_now=True)
