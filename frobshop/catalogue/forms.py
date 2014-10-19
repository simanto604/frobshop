from oscar.apps.dashboard.catalogue.forms import ProductForm as NewProductForm

class ProductForm(NewProductForm):
    def set_initial_attribute_values(self, kwargs):
        if kwargs.get('instance', None) is None:
            return
        if 'initial' not in kwargs:
            kwargs['initial'] = {}
        for attribute in self.product_class.attributes.all():
            try:
                att_values = kwargs['instance'].attribute_values.filter(
                    attribute=attribute)
                values_list = []
                for value in att_values:
                    values_list.append(value.value_entity.name)
                values = ",".join(values_list)
            except ProductAttributeValue.DoesNotExist:
                pass
            else:
                kwargs['initial']['attr_%s' % attribute.code] = values

