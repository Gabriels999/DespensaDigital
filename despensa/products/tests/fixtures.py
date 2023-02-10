from ..models import Product


def product_ketchup():
    ketchup = Product.objects.create(
        id=1,
        name="Ketchup",
        type="Secos",
        price=14.9,
        target_quantity=1,
        real_quantity=0,
    )
    return ketchup


def product_maionese():
    maionese = Product.objects.create(
        id=2,
        name="Maionese",
        type="Secos",
        price=14.9,
        target_quantity=2,
        real_quantity=1,
    )
    return maionese


def product_mostarda():
    mostarda = Product.objects.create(
        id=3,
        name="Mostarda",
        type="Secos",
        price=17.9,
        target_quantity=2,
        real_quantity=2,
    )
    return mostarda
