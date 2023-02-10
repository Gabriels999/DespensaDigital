# coding: utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..commons.django_views_utils import ajax_login_required
from .service import product_svc


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
    return JsonResponse({"products": products})


@csrf_exempt
@ajax_login_required
def use_product(request, id):
    product = product_svc.use_product(id)
    return JsonResponse(product)