from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	birthday = models.CharField(max_length=20, blank=True)
	bio = models.TextField()
	contacts = models.TextField()

	def __unicode__(self):
		return self.name+' '+self.surname

	class Meta:
		db_table = 'contact'
