from ..models import Product, UserStore
from ...accounts.models import Profile
from ...accounts.tests.fixtures import profile_jon


def product_ketchup():
    ketchup = Product.objects.create(
        id=1,
        name="Ketchup",
        type="Secos",
        price=14.9,
    )
    return ketchup


def product_maionese():
    maionese = Product.objects.create(
        id=2,
        name="Maionese",
        type="Secos",
        price=14.9,
    )
    return maionese


def product_mostarda():
    mostarda = Product.objects.create(
        id=3,
        name="Mostarda",
        type="Secos",
        price=17.9,
    )
    return mostarda


def jon_ketchup():
    profile_jon()
    product = product_ketchup()
    ketchup_registrado = UserStore.objects.create(
        owner=Profile.objects.get(user__username='jon'),
        product=product,
        target_quantity=1,
        real_quantity=0,
    )
    return ketchup_registrado
