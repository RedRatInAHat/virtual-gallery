from django.db import models
from years_db.models import YearsInfo, ThemesInfo


class ImagesInfo(models.Model):
    year_choices = {(year.permalink[1:-1], year.permalink[1:-1]) for year in YearsInfo.objects.all().order_by('permalink')}
    themes_choice = {(theme.permalink, theme.permalink) for theme in ThemesInfo.objects.all()}
    themes_choice.add(('', ''))
    title = models.CharField('Title', max_length=60)
    year_link = models.CharField('Year', max_length=60, choices=year_choices)
    theme_link = models.CharField('Theme', max_length=60, blank=True, choices=themes_choice)
    image_file = models.ImageField('File', upload_to='uploaded_images/')
    creation_date = models.DateField('Date of creation', blank=True)
    description = models.TextField('Description', blank=True)
