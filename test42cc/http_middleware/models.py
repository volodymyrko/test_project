from django.db import models

# Create your models here.

class HttpRequestStore(models.Model):
    """ present http request in db
    """
    path = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    remote_address = models.CharField(max_length=10)

    def __unicode__(self):
        return self.path[:10]

    class Meta:
        db_table = 'http_request'
