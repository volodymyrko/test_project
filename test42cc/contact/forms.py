from django.forms import ModelForm
from contact.models import Contact

class ContactForm(ModelForm):
    """ form for contact edit
    """
    class Meta:
        model = Contact
