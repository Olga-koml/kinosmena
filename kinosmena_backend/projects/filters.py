from django_filters.rest_framework import FilterSet, filters
from .models import Project

# TODO Фильтр не подключен, возможно надо удалить, если не будет дополненинй


class ProjectFilter(FilterSet):
    """
    Фильтр заявок по id Проекта.

    Пример фильтра /api/projects/?is_archive=true
    """

    is_archive = filters.BooleanFilter(field_name='is_archive')

    class Meta:
        model = Project
        fields = ['is_archive']
