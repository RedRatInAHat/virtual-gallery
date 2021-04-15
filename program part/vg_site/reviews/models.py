from django.db import models


class Reviews(models.Model):
    review_type_choices = {('review', 'review'), ('suggestion', 'suggestion')}

    review_type = models.CharField("Review Type: ", max_length=10, choices=review_type_choices)
    review_text = models.TextField("Text: ")
    name = models.CharField("From: ", max_length=60, default='Unknown')
    active = models.BooleanField("Active", default=True)
    creation_date = models.DateTimeField("Date of creation", auto_now=True)


class ReviewsPages(models.Model):
    title = models.CharField('Title', max_length=60)
    permalink = models.CharField('Permalink', max_length=20, unique=True)
    nav_title = models.CharField('Navigation Title', max_length=60)
    main_text = models.TextField('Main Text', blank=True)
    update_date = models.DateTimeField('Last Updated', auto_now=True)
