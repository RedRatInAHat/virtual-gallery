from django.shortcuts import render, get_object_or_404
from pages_info.models import PageInfo
from years_db.models import YearsInfo


def index(request, pagename):
    pagename = '/' + pagename
    pg_info = get_object_or_404(PageInfo, permalink=pagename)
    context = {
        'title': pg_info.title,
        'nav_title': pg_info.nav_title,
        'content': pg_info.main_text,
        'pages_list': PageInfo.objects.all(),
    }
    return render(request, 'gallery/main_page.html', context)


def get_year_info(request, pagename, year):
    pagename = '/' + pagename
    year = '/' + year + '/'
    year_info = get_object_or_404(YearsInfo, permalink=year)
    context = {
        'title': year_info.title,
        'content': year_info.main_text,
        'parent_link': pagename,
        'year': year,
        'pages_list': PageInfo.objects.all(),
        'years_list': YearsInfo.objects.all(),
    }
    return render(request, 'gallery/year_page.html', context)
