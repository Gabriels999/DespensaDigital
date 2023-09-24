# coding: utf-8
import json

from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..products.service import log_svc


@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    # if request.method == "POST":
    #     data = json.loads(request.body.decode("utf-8"))
    #     username = data.get("username")
    #     password = data.get("password")
    user = auth.authenticate(username=username, password=password)
    print(user)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        new_user = User.objects.create(username=username, password=make_password(password))
        log_svc.log_signup(new_user)
    return JsonResponse({'message': 'Usuário criado com sucesso.'}, safe=False)


def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return JsonResponse({})


def whoami(request):
    i_am = (
        {
            "user": _user2dict(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    return JsonResponse(i_am)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }
    return d
