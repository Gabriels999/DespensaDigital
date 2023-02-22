from django.contrib.auth.models import User


def test_criar_produto_sem_login(client):
    resp = client.post('/api/products/register_product', {"id": 1, "name": 'Ketchup', "price": 14.9, "type": 'Secos'})
    assert resp.status_code == 401


def test_criar_produto_com_login(client, profile_jon):
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/register_product', {"id": 1, "name": 'Ketchup', "price": 14.9, "type": 'Secos'})
    data = resp.json()
    assert resp.status_code == 200
    assert data == {
        'id': 1,
        'name': 'Ketchup',
        'price': 14.9,
        'type': 'Secos',
    }


def test_criar_produto_e_adicionar_a_despensa_com_login(client, profile_jon):
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/register_product', {
        "id": 1, "name": 'Ketchup', "price": 14.9, "type": 'Secos', "target_quantity": 1, "real_quantity": 0
        })
    data = resp.json()
    assert resp.status_code == 200
    assert len(data) == 2


def test_adicionar_produto_na_despensa_sem_login(client, db):
    resp = client.post('/api/products/add_product')
    assert resp.status_code == 401


def test_adicionar_produto_na_despensa_com_login(client, profile_jon, logged_jon, ketchup):
    resp = client.post('/api/products/add_product', {"id": 1, "target_quantity": 1, "real_quantity": 0})
    data = resp.json()
    assert resp.status_code == 200
    assert len(data) == 2


def test_lista_produtos_sem_login(client, db):
    resp = client.get('/api/products/list_products')
    assert resp.status_code == 401


def test_lista_produtos_com_login(client, db, jon_ketchup):
    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/products/list_products')
    data = resp.json()
    assert resp.status_code == 200
    assert len(data.get('products')) == 1


def test_lista_todos_produtos_com_login(client, db, jon_ketchup):
    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/products/list_all_products')
    data = resp.json()
    assert resp.status_code == 200
    assert data == {
        'products': [
            {
                "id": 1,
                "name": "Ketchup",
                "price": 14.9,
                "type": "Secos"
            }
        ]
    }


def test_edita_produto_sem_login(client, db):
    resp = client.post('/api/products/edit_product/2')
    assert resp.status_code == 401


def test_edita_produto_com_login(client, db, jon_ketchup):
    client.force_login(User.objects.get(username='jon'))
    product_to_update = {
        'id': 1,
        'target_quantity': 3,
    }
    resp = client.post('/api/products/edit_product/1', product_to_update)
    data = resp.json()
    assert resp.status_code == 200
    assert len(data) == 2


def test_remove_product(client, db, jon_ketchup):
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/remove_product/1')
    data = resp.json()

    assert resp.status_code == 200
    assert data == {'products': []}


def test_usar_produto_sem_login(client, db):
    resp = client.post('/api/products/use_product/1')
    assert resp.status_code == 401


def test_usar_produto_com_login(client, db, jon_maionese):
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/use_product/2')
    data = resp.json()
    assert resp.status_code == 200
    assert len(data) == 2


def test_usar_produto_sem_estoque(client, db, jon_ketchup):
    client.force_login(User.objects.get(username='jon'))
    resp = client.post('/api/products/use_product/1')
    data = resp.json()
    assert resp.status_code == 200
    assert len(data) == 2


def test_gerar_lista_de_compra(client, db, jon_ketchup):
    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/products/shopping_list')
    data = resp.json()

    assert resp.status_code == 200
    assert len(data['products']) == 1


def test_comprar_produto(client, db, jon_ketchup):
    client.force_login(User.objects.get(username='jon'))
    resp = client.get('/api/products/shop_product/1')
    data = resp.json()
    print(data)
    assert resp.status_code == 200
    assert len(data) == 2
