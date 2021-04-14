from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review_type', 'creation_date', 'active')
    ordering = ('creation_date', 'active')
    search_fields = ('review_type', 'creation_date', 'active')


admin.site.register(Reviews, ReviewsAdmin)