# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from contact.models import Contact
from contact.forms import ContactForm

def index(request):
    """views for index '/ request, that represent contacts
    """
    query = Contact.objects.all()[:1]
    contact = get_object_or_404(query,)
    return render_to_response('contact.html', {'contact': contact},
        context_instance=RequestContext(request))

@login_required
def edit(request):
    contact = Contact.objects.all()[:1].get()
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

    return render_to_response('edit.html', {'form': form},
        context_instance=RequestContext(request))
