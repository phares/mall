from django.utils.translation import ugettext_lazy as _
from django_tables2 import A, Column, LinkColumn, TemplateColumn
from oscar.core.loading import get_class, get_model

DashboardTable = get_class('dashboard.tables', 'DashboardTable')
CarouselItem = get_model("promotions", "CarouselItem")

class CarouselItemTable(DashboardTable):
    title = LinkColumn('dashboard:carousel-item-edit', args=[A('pk')])
    description = Column(verbose_name=_('Brand description'))
    actions = TemplateColumn(
        template_name='dashboard/catalogue/carousel_row_actions.html',
        orderable=False)

    class Meta(DashboardTable.Meta):
        model = CarouselItem
        fields = ('title', 'description')
