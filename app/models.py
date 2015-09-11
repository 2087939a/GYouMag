from django.db import models
from django.db.models import DateTimeField
from django.db.models import FileField
from datetime import datetime
from django.template.defaultfilters import slugify
from django.core.files.storage import FileSystemStorage



# Create your models here.
# fs = FileSystemStorage(location='/media/images')



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default = 0)
    slug = models.SlugField(unique = True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)
    		
    def __unicode__(self):
	    return self.name
    
class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    content = models.TextField()
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date created', default=datetime.now, blank = True)
    author = models.CharField(max_length=128, default = "someone")
    slug = models.SlugField(unique = True, default = "")
    image = models.ImageField(upload_to = "images/", default = "hank-moody.jpg")
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args,**kwargs)

    
    def __unicode__(self):#For Python 2, use __str__ on Python 3
      return unicode(self.title)
