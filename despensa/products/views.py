# coding: utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import product_svc


@csrf_exempt
@ajax_login_required
def add_product_to_UserStore(request):
    product = product_svc.add_product_to_UserStore(request.POST, request.user.id)
    return JsonResponse(product)


@csrf_exempt
@ajax_login_required
def register_product(request):
    product = product_svc.register_product(request.POST, request.user.id)
    return JsonResponse(product)


@ajax_login_required
def list_all_products(request):
    products = product_svc.list_all_products()
    return JsonResponse({'products': products})


@ajax_login_required
def list_products(request):
    products = product_svc.list_products(request.user.id)
    return JsonResponse({'products': products})


@csrf_exempt
@ajax_login_required
def edit_product(request, id):
    product = product_svc.edit_product(request.POST, request.user.id)
    return JsonResponse(product)


@csrf_exempt
@ajax_login_required
def remove_product(request, id):
    products = product_svc.remove_product(request.user.id, id)
    return JsonResponse({"products": products})


@csrf_exempt
@ajax_login_required
def use_product(request, id):
    product = product_svc.use_product(request.user.id, id)
    return JsonResponse(product)


@ajax_login_required
def shopping_list(request):
    products = product_svc.shopping_list(request.user.id)
    return JsonResponse({'products': products})


@csrf_exempt
@ajax_login_required
def shop_product(request, id):
    product = product_svc.shop_product(request.user.id, id)
    return JsonResponse(product)
