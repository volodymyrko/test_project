# Create your views here.

from django.shortcuts import render_to_response, get_list_or_404
from http_middleware.models import HttpRequestStore

def requests(request):
	request_list = HttpRequestStore.objects.order_by('-time')[:10]
	return render_to_response('requests.html', {'request_list': request_list})

