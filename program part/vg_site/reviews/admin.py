from django.contrib import admin
from .models import Reviews, ReviewsPages


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review_type', 'creation_date', 'active')
    ordering = ('creation_date', 'active')
    search_fields = ('review_type', 'creation_date', 'active')


admin.site.register(Reviews, ReviewsAdmin)


class ReviewsPagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'nav_title', 'update_date')
    ordering = ('pk',)
    search_fields = ('title', 'nav_title')


admin.site.register(ReviewsPages, ReviewsPagesAdmin)
