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


def remove_product(user_id, id):
    product_in_UserStore = UserStore.objects.filter(
        owner=Profile.objects.get(user__id=user_id),
        product=Product.objects.get(id=id)
    )
    product_in_UserStore.delete()
    products_list = UserStore.objects.filter(owner=Profile.objects.get(user__id=user_id))
    return [product.to_dict_json() for product in products_list]


def use_product(user_id, id):
    product = UserStore.objects.filter(
        owner=Profile.objects.get(user__id=user_id),
        product=Product.objects.get(id=id),
    )
    if product.values('real_quantity').first().get('real_quantity') > 0:
        product.update(
            real_quantity=F('real_quantity')-1
        )
    return product[0].to_dict_json()


def shopping_list(user_id):
    products = UserStore.objects.filter(
        owner=Profile.objects.get(user__id=user_id),
        real_quantity__lt=F('target_quantity'))
    return [product.to_dict_json() for product in products]


def shop_product(id):
    product = Product.objects.get(id=id)
    product.real_quantity += 1
    product.save()
    return product.to_dict_json()
