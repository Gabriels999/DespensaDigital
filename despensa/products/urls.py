from django.urls import path

from . import views

urlpatterns = [
    # Related to user logged in
    path('add_product', views.add_product_to_UserStore, name='add_product'),
    path('list_products', views.list_products, name='list_product'),
    path('edit_product/<id>', views.edit_product, name='edit_product'),
    path('remove_product/<id>', views.remove_product, name='remove_product'),

    path('use_product/<id>', views.use_product, name='use_product'),
    path('shop_product/<id>', views.shop_product, name='shop_product'),
    path('shopping_list', views.shopping_list, name='shopping_list'),

    # Related to product
    path('list_all_products', views.list_all_products, name='list_all_products'),
    path('register_product', views.register_product, name='register_product'),  # todo no front
]
