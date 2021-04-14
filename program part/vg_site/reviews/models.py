from django.db import models


class Reviews(models.Model):
    review_type_choices = {('review', 'review'), ('suggestion', 'suggestion')}
    review_type = models.CharField("Review Type: ", max_length=10, choices=review_type_choices)
    review_text = models.TextField("Text: ")
    name = models.CharField('From: ', max_length=60, default='Unknown')
