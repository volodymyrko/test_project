# Create your views here.

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from http_middleware.models import HttpRequestStore

RECORDS_BY_PAGE = 10

def requests(request):
    """ show http requests stored (order_by middleware) in db
    """
    all_request = HttpRequestStore.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_request, RECORDS_BY_PAGE)
    try:
        requests = paginator.page(page)
    except EmptyPage:
        requests = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        requests = paginator.page(1)

    return render_to_response('requests.html', {'requests': requests})

