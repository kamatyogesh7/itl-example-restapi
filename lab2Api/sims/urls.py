from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', views.api_root),
    path('docs/', include_docs_urls(title='Sales And Inventory Management System', description='RESTful API for SIMS')),
    path('Supplier/', views.SupplierListView, name="supplierlist"),
    path('Supplier/<int:pk>', views.SupplierDetailView, name="supplierdetail"),
    path('Inventory/', views.InventoryView.as_view({'get': 'list', 'post': 'create'}), name="inventorylist"),
    path('Inventory/<int:pk>', views.InventoryView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
        name='inventorydetail'),
    path('api-auth',include('rest_framework.urls'))
]