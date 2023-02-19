from ...accounts.models import Profile
from ..models import Product, UserStore
from django.db.models import F


def list_products(id):
    products = UserStore.objects.filter(owner=Profile.objects.get(user__id=id))
    return [product.to_dict_json() for product in products]


def add_product(new_product, userId):
    product = Product(
            name=new_product['name'],
            price=float(new_product['price']),
            type=new_product['type'],
            target_quantity=int(new_product['target_quantity']),
            real_quantity=int(new_product['real_quantity'])
        )
    product.save()
    logged_user = Profile.objects.get(user__id=userId)
    product_user_store = UserStore(
        owner=logged_user,
        product=product
    )
    product_user_store.save()
    return product.to_dict_json()


def register_product(new_product):
    product = Product(
            name=new_product['name'],
            price=float(new_product['price']),
            type=new_product['type'],
        )
    product.save()
    return product.to_dict_json()


def edit_product(new_version_product, id):
    Product.objects.filter(id=id).update(
        name=new_version_product['name'],
        price=new_version_product['price'],
        type=new_version_product['type'],
        target_quantity=new_version_product['target_quantity'],
        real_quantity=new_version_product['real_quantity'],
    )
    new_product = Product.objects.get(id=id)
    return new_product.to_dict_json()


def delete_product(id):
    product = Product.objects.get(id=id)
    product.delete()
    products_list = Product.objects.all()
    return [product.to_dict_json() for product in products_list]


def use_product(id):
    product = Product.objects.get(id=id)
    if product.real_quantity > 0:
        product.real_quantity -= 1
        product.save()
    return product.to_dict_json()


def shopping_list():
    products = Product.objects.filter(real_quantity__lt=F('target_quantity'))
    return [product.to_dict_json() for product in products]


def shop_product(id):
    product = Product.objects.get(id=id)
    product.real_quantity += 1
    product.save()
    return product.to_dict_json()
