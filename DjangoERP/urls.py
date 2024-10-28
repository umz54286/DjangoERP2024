"""
URL configuration for DjangoERP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from erp.views import dashboard, products,insertProducts, modifyProducts,purchaseOrders, insertPurchaseOrders, modifyPurchaseOrders, suppliers, insertSuppliers, modifySuppliers, orders, insertOrders, modifyOrders, customers, insertCustomers, modifyCustomers, inventories, inventoryReport


urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}, name='static')
    path("", dashboard),
    path("products", products),
    path("products/insert", insertProducts),
    path("products/modify", modifyProducts),

    path("purchaseOrders", purchaseOrders),
    path("purchaseOrders/insert", insertPurchaseOrders),
    path("purchaseOrders/modify", modifyPurchaseOrders),

    path("suppliers", suppliers),
    path("suppliers/insert", insertSuppliers),
    path("suppliers/modify", modifySuppliers),

    path("orders", orders),
    path("orders/insert", insertOrders),
    path("orders/modify", modifyOrders),

    path("customers", customers),
    path("customers/insert", insertCustomers),
    path("customers/modify", modifyCustomers),

    path("inventories", inventories),

    path("inventoryReport", inventoryReport),
]
