# yourproject/catalogue/models.py
from django.utils.translation import ugettext_lazy as _
from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProductImage, AbstractProduct


class Product(AbstractProduct):
    brand_name = models.CharField(_('Brand'), max_length=255, blank=True, null=True)
    designer = models.TextField(_('Designer'), blank=True, null=True)
    style = models.CharField(_('Style'), max_length=255, blank=True, null=True)
    
class SizeNFit(models.Model):
	fit = models.CharField(_('Fit'), max_length=255, blank=True, null=True)
	measurement = models.TextField(_('Measurements'), blank=True, null=True)
	model_measurement = models.TextField(_('Model Measurements'), blank=True, null=True)
	size_table = models.TextField(_('Size Table'), blank=True, null=True)
	description = models.TextField(_('Description'), blank=True, null=True)
	product = models.ForeignKey(Product, null=True, blank=True, related_name="product_sizenfit")

	def __unicode__(self):
		return self.fit

from oscar.apps.catalogue.models import *