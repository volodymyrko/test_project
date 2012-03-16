# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from contact.models import Contact


def index(request):
    """views for index '/ request, that represent contacts
    """
    query = Contact.objects.all()[:1]
    contact = get_object_or_404(query,)
    return render_to_response('contact.html', {'contact': contact},
        context_instance=RequestContext(request))
