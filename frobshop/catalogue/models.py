# yourproject/catalogue/models.py
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from oscar.apps.catalogue.abstract_models import AbstractProductImage, AbstractProduct


class Product(AbstractProduct):
    product_id = models.CharField(_('Product ID'), max_length=100, blank=True, unique=True)
    product_sku = models.CharField(_('Product SKU'), max_length=100, blank=True, null=True)
    brand_name = models.CharField(_('Brand'), max_length=255, blank=True, null=True)
    # designer = models.TextField(_('Designer'), blank=True, null=True)
    # # title = models.CharField(_('Title'), max_length=255, blank=True, null=True)
    # style = models.CharField(_('Style'), max_length=255, blank=True, null=True)
    
    @property
    def get_brand(self):
        """
        Return a product's brand name
        """
        brand = self.brand_name
        if not brand:
            brand = 'Brand Name'
        return brand



class RelatedProduct(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name="product_releted_by_id")
    releted_product_id = models.CharField(_('Related Product ID'), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.product_id

    
class SizeNFit(models.Model):
	fit = models.CharField(_('Fit'), max_length=255, blank=True, null=True)
	measurement = models.TextField(_('Measurements'), blank=True, null=True)
	model_measurement = models.TextField(_('Model Measurements'), blank=True, null=True)
	size_table = models.TextField(_('Size Table'), blank=True, null=True)
	description = models.TextField(_('Description'), blank=True, null=True)
	product = models.ForeignKey(Product, null=True, blank=True, related_name="product_sizenfit")

	def __unicode__(self):
		return self.fit
	    

	
	
class ProductColor(models.Model):
    '''
    Color and Color thumbnail of product image
    '''
    product = models.ForeignKey(Product, null=True, blank=True, related_name="product_color")
    color = models.CharField(_('Color'), max_length=255, blank=True, null=True)
    color_thumbnail = models.ImageField(upload_to = 'color_thumnails/' ,  blank=True, null=True)
    shopbop_color_thumnail_url = models.CharField(_('Shopbop Color Thumbnail Url'), max_length=1000, blank=True, null=True)
    primary_color = models.BooleanField(default = False)
    color_order = models.IntegerField()

    class Meta:
        ordering = ['color_order']
    
    def __unicode__(self):
        return self.color


class ProductImage(AbstractProductImage):
    shopbop_thumb_url = models.CharField(_('Shopbop Thumb Url'), max_length=1000, blank=True, null=True)
    shopbop_big_image_url = models.CharField(_('Shopbop Big Image Url'), max_length=1000, blank=True, null=True)

class ProductSize(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name="product_size")
    size = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        if not self.size:
            self.size = None
        return self.size
    

from oscar.apps.catalogue.models import *