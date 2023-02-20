from ...accounts.models import Profile
from ..models import Product, UserStore
from django.db.models import F, Q


def list_products(id):
    products = UserStore.objects.filter(owner=Profile.objects.get(user__id=id))
    return [product.to_dict_json() for product in products]


def add_product_to_UserStore(new_product, user_id):
    product = Product.objects.get(id=new_product['id'])
    logged_user = Profile.objects.get(user__id=user_id)
    product_user_store = UserStore(
        owner=logged_user,
        product=product,
        target_quantity=int(new_product['target_quantity']),
        real_quantity=int(new_product['real_quantity'])
    )
    product_user_store.save()
    return product_user_store.to_dict_json()


def register_product(new_product):
    product = Product(
            name=new_product['name'],
            price=float(new_product['price']),
            type=new_product['type'],
        )
    product.save()
    return product.to_dict_json()


def edit_product(new_version_product, user_id):
    product_to_update = UserStore.objects.filter(
        Q(owner=Profile.objects.get(user__id=user_id)),
        Q(product=Product.objects.get(id=new_version_product.get('id')))
    )
    product_to_update.update(
        target_quantity=int(new_version_product.get('target_quantity'))
    )
    updated_product = UserStore.objects.get(product__id=new_version_product.get('id'))
    return updated_product.to_dict_json()


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
