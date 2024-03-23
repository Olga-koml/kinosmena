from drf_yasg import openapi

#  Параметры натройки для свагера, фильтр проектов в ЛК

archive_project_filter_param = [
    openapi.Parameter(
        'is_archive', openapi.IN_QUERY, type=openapi.TYPE_STRING,
        description=('Фильтрует проекты пользователя в архиве.\n'
                     'Пример запроса /projects/?is_archive=true')
    ),
]

shifts_filter_params = [
    openapi.Parameter(
        'project', openapi.IN_QUERY, type=openapi.TYPE_STRING,
        description=('Фильтрует смены пользователя по id проекта.\n'
                     'Пример запроса /shifts/?project=1')
    ),
    openapi.Parameter(
        'start_date_from', openapi.IN_QUERY, type=openapi.TYPE_STRING,
        description=('Фильтрует смены пользователя с указанной даты в формате yyyy-mm-dd.\n'
                     'Пример запроса /shifts/?start_date_from=2020-01-01')
    ),
    openapi.Parameter(
        'start_date_to', openapi.IN_QUERY, type=openapi.TYPE_STRING,
        description=('Фильтрует смены пользователя до указаной даты в формате yyyy-mm-dd.\n'
                     'Пример запроса /shifts/?start_date_to=2020-01-01')
    ),
    openapi.Parameter(
        'is_active', openapi.IN_QUERY, type=openapi.TYPE_STRING,
        description=('Фильтрует активные (открытые) смены пользователя.\n'
                     'Пример запроса /shifts/?is_active=true')
    ),
]
