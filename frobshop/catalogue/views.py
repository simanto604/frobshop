from oscar.apps.catalogue.views import ProductDetailView as ProductDetailViewNew
from oscar.apps.catalogue.views import ProductCategoryView as ProductCategoryViewNew


class ProductDetailView(ProductDetailViewNew):
	template_folder = "verecom/catalogue"
	# pass


class ProductCategoryView(ProductCategoryViewNew):
	template_name = 'verecom/catalogue/browse.html'