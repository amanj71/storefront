from django.urls import path
from . import views

# URLConfigs

urlpatterns = [
    path('products/', views.product_list, name="anything"),
    path('products/<int:id>/', views.product_detail, name="ing"),
    path('collections/<int:id>/', views.collection_detail, name="collection"),
]