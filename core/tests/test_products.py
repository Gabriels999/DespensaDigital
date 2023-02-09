from core.models import User, Product
from core.tests import fixtures

produto ={
    "id": 1,
    "name": "Ketchup",
    "type": "Secos",
    "price": 10.9,
    "target_quantity": 1,
    "real_quantity": 0,
  }

def test_criar_produto_sem_login(client):
    resp = client.post('/api/add_product', produto)
    assert resp.status_code == 401


def test_criar_produto_com_login(client, db):
    fixtures.user_jon()
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/add_product', produto)
    assert resp.status_code == 200


def test_lista_produtos_sem_login(client, db):
    resp = client.get('/api/list_products')
    assert resp.status_code == 401


def test_lista_produtos_com_login(client, db):
    fixtures.user_jon()
    fixtures.product_ketchup()

    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/list_products')
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
    resp = client.post('/api/edit_product/2')
    assert resp.status_code == 401


def test_edita_produto_com_login(client, db):
    fixtures.user_jon()
    fixtures.product_ketchup()
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/edit_product/1', produto)
    data = resp.json()
    
    assert resp.status_code == 200
    assert data == {
        'id': produto['id'],
        'name': produto['name'],
        'price': produto['price'],
        'target_quantity': produto['target_quantity'],
        'real_quantity': produto['real_quantity'],
        'type': produto['type'],
    }