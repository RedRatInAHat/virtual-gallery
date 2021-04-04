from django.contrib import admin
from .models import PageInfo


class PageInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'nav_title', 'update_date')
    ordering = ('pk',)
    search_fields = ('title', 'nav_title')


admin.site.register(PageInfo, PageInfoAdmin)
