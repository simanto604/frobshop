from frobshop.catalogue.models import ProductClass


def product_class(request):
	product_types = ProductClass.objects.all()

	return {"product_types": product_types}