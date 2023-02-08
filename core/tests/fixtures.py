from core.models import User, Product


def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze

def product_ketchup():
    ketchup = Product.objects.create(
        id=1,
        name="Ketchup",
        type= "Secos",
        price= 14.9,
        target_quantity= 1,
        real_quantity= 0,
    )
    return ketchup