from rest_framework import generics

from products.models import Category
from products.paginators import CustomPaginator
from products.serializers import CategorySerializer, CategoryWithSubcategoriesSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPaginator


class CategoryRetrieveView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryWithSubcategoryRetrieveView(generics.RetrieveAPIView):
    serializer_class = CategoryWithSubcategoriesSerializer
    queryset = Category.objects.all()
