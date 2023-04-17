from django.urls import path
from rest_framework.routers import DefaultRouter

from . import viewsets, views

app_name = "products"

router = DefaultRouter()
router.register(r"products", viewsets.ProductViewSet, basename="product")

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("categories/<int:pk>/", views.CategoryRetrieveView.as_view(), name="categories"),
    path("categories/<int:pk>/subcategories/", views.CategoryWithSubcategoryRetrieveView.as_view(),
         name="categories_with_subcategories"),
    *router.urls
]
