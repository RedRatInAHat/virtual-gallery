from django.contrib import admin
from .models import YearsInfo, ThemesInfo


class YearsInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('pk',)
    search_fields = ('title',)


class ThemesInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'update_date')
    ordering = ('year',)
    search_fields = ('title',)


admin.site.register(YearsInfo, YearsInfoAdmin)
admin.site.register(ThemesInfo, ThemesInfoAdmin)
