from django_filters import rest_framework as filters

from reports.models import Report


class ReportFilter(filters.FilterSet):
    tid = filters.CharFilter(field_name='user', method='filter_user')
    start_date_from = filters.DateFilter(field_name='start_date', lookup_expr='gte')
    start_date_to = filters.DateFilter(field_name='start_date', lookup_expr='lte')

    def filter_user(self, queryset, name, value):
        return queryset.filter(user=value)

    class Meta:
        model = Report
        fields = ['project', 'start_date_from', 'start_date_to']