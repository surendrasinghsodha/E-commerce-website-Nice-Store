import django_tables2 as tables
from django.utils.html import format_html

from myapp.models import Category, Product


class CategoryTable(tables.Table):
    # add column in table
    action = tables.TemplateColumn(verbose_name="Action",
                                   template_name="myapp/category/action_table.html")

    class Meta:
        model = Category
        fields = ('category_name', 'created_by', 'created_at')


class ViewProductTable(tables.Table):  # from here ve go to views and make (SingleTableView)
    action = tables.TemplateColumn(verbose_name="Action",
                                   template_name="myapp/seller/update_delete.html")

    class Meta:
        model = Product
        fields = ['id', 'product_collection', 'product_category',
                  'product_size', 'product_color', 'product_price', 'product_description',
                  'product_image']

    @staticmethod
    def render_product_size(record):  # to give css to column data :
        if record.product_size == 'm':
            return format_html('<span class="badge bg-primary">M</span>')
        else:
            return format_html('<span class="badge bg-danger">L</span>')

    @staticmethod
    def render_product_image(record):
        return format_html('<span class="btn btn-link">Link</span>')
