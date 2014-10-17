# yourproject/catalogue/models.py
from django.utils.translation import ugettext_lazy as _
from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProductImage, AbstractProduct


class Product(AbstractProduct):
    brand_name = models.CharField(_('Brand'), max_length=255, blank=True, null=True)
    designer = models.TextField(_('Designer'), blank=True, null=True)
    style = models.CharField(_('Style'), max_length=255, blank=True, null=True)
    
    @property
    def get_brand(self):
        """
        Return a product's brand name
        """
        brand = self.brand_name
        if not brand:
            brand = 'Brand Name'
        return brand
    
    
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
    color_thumbnail = models.ImageField(upload_to = 'color_thumnails/' ,  blank=True)
    shopbop_color_thumnail_url = models.CharField(_('Shopbop Color Thumbnail Url'), max_length=400, blank=True, null=True)
    primary_color = models.BooleanField(default = False)
    
    def __unicode__(self):
	return self.color


class ProductImage(AbstractProductImage):
    color = models.ForeignKey(ProductColor, null=True, blank=True, related_name="product_image_color")
    shopbop_image_url = models.CharField(_('Shopbop Image Url'), max_length=400, blank=True, null=True)


class ProductSize(models.Model):
    pass
    

from oscar.apps.catalogue.models import *