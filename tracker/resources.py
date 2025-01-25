from import_export import resources, fields
from tracker.models import Transaction, Category
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import DateWidget


class TransactionResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, field='name')
    )

    def before_import_row(self, row, **kwargs):
        category_name = row.get('category')
        if category_name:
            # Get or create the category
            Category.objects.get_or_create(name=category_name)

    date = fields.Field(
        column_name='date',
        attribute='date',
        widget=DateWidget(format='%d-%m-%Y')  # Adjust this format to match the input
    )


    def after_init_instance(self, instance, new, row, **kwargs):
        instance.user = kwargs.get('user')

    class Meta:
        model = Transaction
        fields = (
            'amount',
            'type',
            'date',
            'category',            
        )
        import_id_fields = (
            'amount',
            'type',
            'date',
            'category',              
        )