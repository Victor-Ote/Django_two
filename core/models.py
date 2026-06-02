from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    created_at = models.DateTimeField('created at', auto_now_add=True)
    modified_at = models.DateTimeField('modified at', auto_now=True)
    active = models.BooleanField('Active', default=True)
    
    class Meta:
        abstract = True
        

class Product(models.Model):
    title = models.CharField('title', max_length=100)
    stock = models.IntegerField('stock', default=0)
    price = models.DecimalField('price', max_digits=10, decimal_places=2, default=0)
    description = models.CharField('description', max_length=1000, default='')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    image = StdImageField('image', upload_to='product', variations={'thumb': (230, 230)}, blank=True)
    
    def __str__(self):
        return self.title
    
def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.title)
    
signals.pre_save.connect(product_pre_save, sender=Product)