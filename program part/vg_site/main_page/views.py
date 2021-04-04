from django.shortcuts import render
from pages_info.models import PageInfo


def index(request, pagename):
    pagename = '/' + pagename
    pg_info = PageInfo.objects.get(permalink=pagename)
    context = {
        'title': pg_info.title,
        'nav_title': pg_info.nav_title,
        'content': pg_info.main_text,
        'pages_list': PageInfo.objects.all(),
    }
    return render(request, 'main_page/main.html', context)
