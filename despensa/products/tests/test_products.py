from django.contrib.auth.models import User
from ...accounts.tests.fixtures import user_jon
from . import fixtures

ketchup = {
        "id": 1,
        "name": 'Ketchup',
        "price": 14.9,
        "target_quantity": 1,
        "real_quantity": 0,
        "type": 'Secos',
  }
maionese = {
        "id": 2,
        "name": 'Maionese',
        "price": 14.9,
        "target_quantity": 2,
        "real_quantity": 1,
        "type": 'Secos',
  }


def test_criar_produto_sem_login(client):
    resp = client.post('/api/products/add_product', ketchup)
    assert resp.status_code == 401


def test_criar_produto_com_login(client, db):
    user_jon()
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/add_product', ketchup)
    data = resp.json()
    assert resp.status_code == 200
    assert data == {
        'id': 1,
        'name': 'Ketchup',
        'price': 14.9,
        'target_quantity': 1,
        'real_quantity': 0,
        'type': 'Secos',
    }


def test_lista_produtos_sem_login(client, db):
    resp = client.get('/api/products/list_products')
    assert resp.status_code == 401


def test_lista_produtos_com_login(client, db):
    user_jon()
    fixtures.product_ketchup()

    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/products/list_products')
    data = resp.json()

    assert resp.status_code == 200
    assert data == {
        'products': [
            {
                'id': 1,
                'name': 'Ketchup',
                'price': 14.9,
                'real_quantity': 0,
                'target_quantity': 1,
                'type': 'Secos',
            }
        ]
    }


def test_edita_produto_sem_login(client, db):
    resp = client.post('/api/products/edit_product/2')
    assert resp.status_code == 401


def test_edita_produto_com_login(client, db):
    user_jon()
    fixtures.product_ketchup()
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/edit_product/1', ketchup)
    data = resp.json()

    assert resp.status_code == 200
    assert data == {
        'id': ketchup['id'],
        'name': ketchup['name'],
        'price': ketchup['price'],
        'target_quantity': ketchup['target_quantity'],
        'real_quantity': ketchup['real_quantity'],
        'type': ketchup['type'],
    }


def test_delete_product(client, db):
    user_jon()
    fixtures.product_ketchup()
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/delete_product/1')
    data = resp.json()

    assert resp.status_code == 200
    assert data == {'products': []}


def test_usar_produto_sem_login(client, db):
    resp = client.post('/api/products/use_product/1')
    assert resp.status_code == 401


def test_usar_produto_com_login(client, db):
    user_jon()
    fixtures.product_maionese()
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/use_product/2')
    data = resp.json()

    assert resp.status_code == 200
    assert data == {
        "id": 2,
        "name": 'Maionese',
        "type": 'Secos',
        "price": 14.9,
        "target_quantity": 2,
        "real_quantity": 0,
    }


def test_usar_produto_sem_estoque(client, db):
    user_jon()
    fixtures.product_ketchup()
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/use_product/1')
    data = resp.json()

    assert resp.status_code == 200
    assert data == {
        "id": 1,
        "name": 'Ketchup',
        "type": 'Secos',
        "price": 14.9,
        "target_quantity": 1,
        "real_quantity": 0,
    }


def test_gerar_lista_de_compra(client, db):
    user_jon()
    fixtures.product_ketchup()
    fixtures.product_maionese()
    fixtures.product_mostarda()
    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/products/shopping_list')
    data = resp.json()

    assert resp.status_code == 200
    assert len(data['products']) == 2


def test_comprar_produto(client, db):
    user_jon()
    fixtures.product_ketchup()
    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/products/shop_product/1')
    data = resp.json()

    assert resp.status_code == 200
    assert data == {
        "id": 1,
        "name": "Ketchup",
        "type": "Secos",
        "price": 14.9,
        "target_quantity": 1,
        "real_quantity": 1,
    }
