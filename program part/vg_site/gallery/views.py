from django.shortcuts import render, get_object_or_404
from pages_info.models import PageInfo


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
