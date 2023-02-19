from django.urls import path

from . import views

urlpatterns = [
    # Related to user logged in
    path('list_products', views.list_products, name='list_product'),
    path('add_product', views.add_product, name='add_product'),

    path('use_product/<id>', views.use_product, name='use_product'),
    path('shop_product/<id>', views.shop_product, name='shop_product'),
    path('shopping_list', views.shopping_list, name='shopping_list'),

    # Related to product
    path('register_product', views.register_product, name='register_product'),
    path('edit_product/<id>', views.edit_product, name='edit_product'),
    path('delete_product/<id>', views.delete_product, name='delete_product'),

]
