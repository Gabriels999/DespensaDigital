from core.models import Product

def list_products():
    products = Product.objects.all()
    return [product.to_dict_json() for product in products]


def add_product(new_product):
    product = Product(
            name=new_product['name'],
            price=float(new_product['price']),
            type=new_product['type'],
            target_quantity=int(new_product['target_quantity']),
            real_quantity=int(new_product['real_quantity'])
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


def use_product(id):
    product = Product.objects.get(id=id)
    if product.real_quantity > 0:
        product.real_quantity -= 1
        product.save()
    return product.to_dict_json()