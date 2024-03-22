from users.models import TelegramUser
from django.urls import reverse


def get_user_tid(request):
    tid = request.GET.get('tid')
    user, create = TelegramUser.objects.get_or_create(
        tid=tid
    )

    return user


class GetOrCreateUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            if request.method == 'GET':
                get_user_tid(request)
        response = self.get_response(request)

        return response
