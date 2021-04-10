from django.contrib import admin
from .models import YearsInfo


class YearsInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('pk',)
    search_fields = ('title',)


admin.site.register(YearsInfo, YearsInfoAdmin)
