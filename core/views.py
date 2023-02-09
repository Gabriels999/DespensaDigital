# coding: utf-8
import json
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, product_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


@csrf_exempt
@ajax_login_required
def add_product(request):
    product = product_svc.add_product(request.POST)
    return JsonResponse(product)


@ajax_login_required
def list_products(request):
    products = product_svc.list_products()
    return JsonResponse({'products': products})


@csrf_exempt
@ajax_login_required
def edit_product(request, id):
    product = product_svc.edit_product(request.POST, id)
    return JsonResponse(product)


@csrf_exempt
@ajax_login_required
def delete_product(request, id):
    products = product_svc.delete_product(id)
    return JsonResponse({"products":products})


@csrf_exempt
@ajax_login_required
def use_product(request, id):
    product = product_svc.use_product(id)
    return JsonResponse(product)


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
