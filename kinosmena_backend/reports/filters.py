# import django_filters
#
# from projects.models import Project
# from reports.models import Report
# from users.models import TelegramUser
#
#
# class ReportFilter(django_filters.FilterSet):
#     user = django_filters.ModelChoiceFilter(queryset=TelegramUser.objects.all())
#     project = django_filters.ModelChoiceFilter(queryset=Project.objects.all())
#
#     class Meta:
#         model = Report
#         fields = [
#             'project',
#             'user',
#             'start_date',
#             'end_date'
#         ]
