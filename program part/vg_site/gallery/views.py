from django.shortcuts import render, get_object_or_404
from pages_info.models import PageInfo
from years_db.models import YearsInfo, ThemesInfo
from images.models import ImagesInfo


def index(request, pagename):
    pagename = '/' + pagename
    pg_info = get_object_or_404(PageInfo, permalink=pagename)
    context = {
        'title': pg_info.title,
        'nav_title': pg_info.nav_title,
        'content': pg_info.main_text,
        'pages_list': PageInfo.objects.all(),
        'years_list': YearsInfo.objects.all(),
    }
    return render(request, 'gallery/main_page.html', context)


def get_year_info(request, year):
    year = '/' + year + '/'
    year_info = get_object_or_404(YearsInfo, permalink=year)
    context = {
        'title': year_info.title,
        'content': year_info.main_text,
        'year': year,
        'pages_list': PageInfo.objects.all(),
        'years_list': YearsInfo.objects.all(),
        'themes_list': ThemesInfo.objects.filter(year=year_info.title),
        'images': ImagesInfo.objects.filter(year_link=year[1:-1], theme_link=''),
    }
    return render(request, 'gallery/year_page.html', context)


def get_theme_info(request, year, theme):
    year = '/' + year + '/'
    year_title = get_object_or_404(YearsInfo, permalink=year).title
    theme_info = get_object_or_404(ThemesInfo, permalink=theme, year=year_title)
    context = {
        'title': theme_info.title,
        'year_title': year_title,
        'content': theme_info.main_text,
        'pages_list': PageInfo.objects.all(),
        'years_list': YearsInfo.objects.all(),
        'themes_list': ThemesInfo.objects.filter(year=year_title)
    }
    return render(request, 'gallery/theme_page.html', context)
