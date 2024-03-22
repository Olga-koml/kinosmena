from drf_yasg import openapi

#  Параметры натройки для свагера, фильтр проектов в ЛК

archive_project_filter_param = [
    openapi.Parameter(
        'is_archive', openapi.IN_QUERY, type=openapi.TYPE_STRING,
        description=('Фильтрует проекты пользователя в архиве.\n'
                     'Пример запроса /projects/?is_archive=true')
    ),
]
