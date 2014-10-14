# myproject/promotions/app.py
from oscar.apps.catalogue.app import CatalogueApplication as CoreCatalogueApplication

from frobshop.catalogue.views import ProductDetailView, ProductCategoryView

class CatalogueApplication(CoreCatalogueApplication):
    detail_view  = ProductDetailView
    category_view = ProductCategoryView

application = CatalogueApplication()