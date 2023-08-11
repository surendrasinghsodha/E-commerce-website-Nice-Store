import django_filters
from myapp.models import Product


class ProductFilter(django_filters.FilterSet):
    # production_description = django_filters.CharFilter(lookup_expr="icontains", widget=TextInput(attrs={'Placeholder':'write the word here'})

    class Meta:
        model = Product
        fields = {'product_description': ['icontains'],
                  'product_collection': ['exact'],
                  'product_size': ['exact'],
                  'product_category': ['exact'],
                  }
