from django.urls import path
from .views import product_list, new_prod


app_name = 'products'
urlpatterns = [
    path('', product_list, name='product_page'),
    path('new/', new_prod, name='new_prod'),
]
