from django.db import models
import Image
# Create your models here.

PHOTO_WIDTH = 300
PHOTO_HEIGHT = 400

class Contact(models.Model):
    """ Model for represent name, surname, bio, contact etc ...
    """
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthday = models.CharField(max_length=20, blank=True)
    bio = models.TextField()
    email = models.EmailField(blank=True)
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=50, blank=True)
    contacts = models.TextField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)

    def __unicode__(self):
        return self.name+' '+self.surname

    class Meta:
        db_table = 'contact'

    def save(self, *args, **kwargs):
        """ rezise image if it's size is more than PHOTO_WIDTH and PHOTO_HEIGHT
        """
        super(Contact, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo.path)
            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')
            width = image.size[0]
            height = image.size[1]
            if PHOTO_WIDTH < width or PHOTO_HEIGHT < height:
                w_ratio = width/float(PHOTO_WIDTH)
                h_ratio = height/float(PHOTO_HEIGHT)
                ratio = w_ratio if w_ratio > h_ratio else h_ratio
                dest_width = width/ratio
                dest_height = height/ratio
                image = image.resize((dest_width, dest_height), Image.ANTIALIAS) 
                image.save(self.photo.path)
