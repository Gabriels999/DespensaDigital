from core.models import Product

def list_products():
    products = Product.objects.all()
    return [product.to_dict_json() for product in products]


def add_product(new_product):
    product = Product(
            name=new_product['name'],
            price=new_product['price'],
            type=new_product['type'],
            target_quantity=new_product['target_quantity'],
            real_quantity=new_product['real_quantity']
        )
    product.save()
    return product.to_dict_json()

def edit_product(new_version_product, id):
    product = Product.objects.get(id=id)
    product.name = new_version_product['name']
    product.price = new_version_product['price']
    product.type = new_version_product['type']
    product.target_quantity = new_version_product['target_quantity']
    product.real_quantity = new_version_product['real_quantity']
    product.save()
    return product.to_dict_json()