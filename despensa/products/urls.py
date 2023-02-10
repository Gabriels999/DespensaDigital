from django.urls import path

from . import views

urlpatterns = [
    path('add_product', views.add_product, name='add_product'),
    path('list_products', views.list_products, name='list_product'),
    path('edit_product/<id>', views.edit_product, name='edit_product'),
    path('delete_product/<id>', views.delete_product, name='delete_product'),

    path('use_product/<id>', views.use_product, name='use_product'),
]
