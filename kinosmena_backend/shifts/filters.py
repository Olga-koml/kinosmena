from django_filters import rest_framework as filters

from shifts.models import Shift


class ShiftFilter(filters.FilterSet):
    start_date_from = filters.DateFilter(
        field_name='start_date', lookup_expr='gte'
    )
    start_date_to = filters.DateFilter(
        field_name='start_date', lookup_expr='lte'
    )
    is_active = filters.BooleanFilter(method='get_is_active')

    def get_is_active(self, queryset, name, value):
        if value:
            queryset = queryset.filter(end_date=None)
        elif not value:
            queryset = queryset.filter(end_date__isnull=False)
        return queryset

    class Meta:
        model = Shift
        fields = ['project', 'start_date_from', 'start_date_to', 'is_active']
