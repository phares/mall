from django.utils.translation import ugettext_lazy as _
from django_tables2 import A, Column, LinkColumn, TemplateColumn
from oscar.core.loading import get_class, get_model

DashboardTable = get_class('dashboard.tables', 'DashboardTable')
Brand = get_model('catalogue', 'Brand')

class BrandTable(DashboardTable):
    name = LinkColumn('dashboard:catalogue-brand-edit', args=[A('pk')])
    slug = Column(verbose_name=_('Brand slug'))
    actions = TemplateColumn(
        template_name='dashboard/catalogue/brand_row_actions.html',
        orderable=False)

    class Meta(DashboardTable.Meta):
        model = Brand
        fields = ('name', 'slug')
