import pytest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


@pytest.fixture()
def user_jon(db):
    ze = User.objects.create(
        username="jon",
        first_name="Jon",
        last_name="Snow",
        email="jon@example.com",
        password=make_password("snow"),
    )
    return ze


@pytest.fixture()
def logged_jon(client, user_jon):
    logged_user = client.force_login(User.objects.get(username='jon'))
    return logged_user
