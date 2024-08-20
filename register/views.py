from django.http import HttpResponse
from django.http import JsonResponse
from .models import Usersinfo 


def user_detail(request,user_id):
    user_instance= Usersinfo.objects.get(id=user_id)
    data = {
        'username': user_instance.username,
        'date': user_instance.published
    }
    res = JsonResponse(data, status=200)
    return res

def firstp (request):
    return HttpResponse("hi this a site for register some users and control them ")