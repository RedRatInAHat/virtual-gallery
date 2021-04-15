from django.shortcuts import render, get_object_or_404
from pages_info.models import PageInfo
from reviews.models import ReviewsPages, Reviews
from .forms import ReviewsForm
from django.http import HttpResponseRedirect


def review_main(request, pagename):
    pagename = '/' + pagename
    pg_info = get_object_or_404(PageInfo, permalink=pagename)
    context = {
        'title': pg_info.title,
        'content': pg_info.main_text,
        'permalink': pagename,
        'pages_list': PageInfo.objects.all(),
        'reviews_pages_list': ReviewsPages.objects.all(),
    }
    return render(request, 'reviews/main_page.html', context)


def review_read(request, pagename, mode):
    pagename = '/' + pagename
    mode = '/' + mode
    pg_info = get_object_or_404(ReviewsPages, permalink=mode)
    context = {
        'title': pg_info.title,
        'content': pg_info.main_text,
        'permalink': pagename,
        'pages_list': PageInfo.objects.all(),
        'reviews_pages_list': ReviewsPages.objects.all(),
        'reviews': Reviews.objects.filter(active=True, review_type='review'),
    }
    return render(request, 'reviews/read_page.html', context)


def review_write(request, pagename, mode):
    pagename = '/' + pagename
    mode = '/' + mode
    submitted = False

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(pagename + mode + '/?submitted=True')
    else:
        form = ReviewsForm()
        if 'submitted' in request.GET:
            submitted = True
    pg_info = get_object_or_404(ReviewsPages, permalink=mode)
    context = {
        'title': pg_info.title,
        'content': pg_info.main_text,
        'permalink': pagename,
        'pages_list': PageInfo.objects.all(),
        'reviews_pages_list': ReviewsPages.objects.all(),
        'reviews': Reviews.objects.filter(active=True, review_type='review'),
        'submitted': submitted,
        'form': form,
    }
    return render(request, 'reviews/write_page.html', context)
