import pytest
from django.contrib.auth.models import User

from ..models import Product, UserStore


@pytest.fixture()
def user_jon(db):
    ze = User.objects.create(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
    )
    return ze


@pytest.fixture()
def logged_jon(client, user_jon):
    logged_user = client.force_login(User.objects.get(username='jon'))
    return logged_user


@pytest.fixture()
def ketchup(db):
    ketchup = Product.objects.create(
        id=1,
        name="Ketchup",
        type="Secos",
        price=14.9,
    )
    return ketchup


@pytest.fixture()
def maionese():
    maionese = Product.objects.create(
        id=2,
        name="Maionese",
        type="Secos",
        price=14.9,
    )
    return maionese


@pytest.fixture()
def jon_ketchup(ketchup, user_jon):
    product = Product.objects.first()
    ketchup_registrado = UserStore.objects.create(
        owner=User.objects.get(username='jon'),
        product=product,
        target_quantity=1,
        real_quantity=0,
    )
    return ketchup_registrado


@pytest.fixture()
def jon_maionese(maionese, user_jon):
    product = Product.objects.first()
    maionese_registrada = UserStore.objects.create(
        owner=User.objects.get(username='jon'),
        product=product,
        target_quantity=3,
        real_quantity=2,
    )
    return maionese_registrada
