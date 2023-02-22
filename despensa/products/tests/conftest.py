from despensa.products.models import User
from ..models import Product, UserStore
from ...accounts.models import Profile

import pytest


@pytest.fixture()
def user_jon(db):
    ze = User.objects.create_user(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password="snow",
    )
    return ze


@pytest.fixture()
def profile_jon(db, user_jon):
    profile = Profile(
        user=User.objects.first(),
        bio='Staff dev',
        avatar='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7b_kyJLpVSVTw48E8LjRICv73BfaKJ9RAtQoYzmD4jwjnWEJ-dMzHInpgP9t10ZQdb6A&usqp=CAU'
    ).save()
    return profile


@pytest.fixture()
def logged_jon(client):
    logged_user = client.force_login(User.objects.get(username='jon'))
    return logged_user


@pytest.fixture()
def ketchup():
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
def jon_ketchup(ketchup, profile_jon):
    product = Product.objects.first()
    ketchup_registrado = UserStore.objects.create(
        owner=Profile.objects.get(user__username='jon'),
        product=product,
        target_quantity=1,
        real_quantity=0,
    )
    return ketchup_registrado


@pytest.fixture()
def jon_maionese(maionese, profile_jon):
    product = Product.objects.first()
    maionese_registrada = UserStore.objects.create(
        owner=Profile.objects.get(user__username='jon'),
        product=product,
        target_quantity=3,
        real_quantity=2,
    )
    return maionese_registrada
