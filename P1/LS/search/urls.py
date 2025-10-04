from django.urls import path
from .views import search_products
from .views_cbv import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = "search"

urlpatterns = [
    # Ruta existente
    path('', search_products, name='search_products'),

    # Nuevas rutas CRUD con CBV
    path('crud/', ProductListView.as_view(), name='list'),
    path('crud/nuevo/', ProductCreateView.as_view(), name='create'),
    path('crud/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('crud/<int:pk>/editar/', ProductUpdateView.as_view(), name='update'),
    path('crud/<int:pk>/eliminar/', ProductDeleteView.as_view(), name='delete'),
]
