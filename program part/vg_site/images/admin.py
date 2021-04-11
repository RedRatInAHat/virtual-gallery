from django.contrib import admin
from .models import ImagesInfo


class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_link', 'theme_link', 'creation_date')
    ordering = ('year_link', 'creation_date')
    search_fields = ('year_link', 'theme_link')


admin.site.register(ImagesInfo, ImageInfoAdmin)
