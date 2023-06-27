from .models import Category, Drinks, VarietyInDrinkCategory
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework import generics
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (CategorySerializer, VarietyInDrinkCategorySerializer,
                          DrinksSerializer)


class GetCategoryInfoView(APIView):
    """Класс для отображения всех активных категорий напитков"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся Категорий"""

        queryset = Category.objects.filter(is_active=True).all()
        serializer_for_queryset = CategorySerializer(instance=queryset, many=True)
        return Response({"categories": serializer_for_queryset.data})


class GetVarietyInDrinkCategoryInfoView(APIView):
    """Класс для отображения всех активных Категорий определенного типа напитков"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся Категорий"""

        queryset = VarietyInDrinkCategory.objects.filter(is_active=True).all()
        serializer_for_queryset = VarietyInDrinkCategorySerializer(instance=queryset, many=True)
        return Response({"variety_in_drink_category": serializer_for_queryset.data})


class GetDrinksInfoView(APIView):
    """Класс для отображения всех активных напитков"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся Категорий"""

        queryset = Drinks.objects.filter(is_active=True).all()
        serializer_for_queryset = DrinksSerializer(instance=queryset, many=True)
        return Response({"drinks": serializer_for_queryset.data})


class GetCategoryDrinksView(generics.ListAPIView):
    """Класс для отображения всех напитков определенной категории"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = DrinksSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        # Получили список всех активных напитков по заданной категории
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(Category, slug=category_slug)
        drinks = category.drinks_set.filter(
            is_active=True
        ).all()

        return drinks


class GetVarietyInDrinkCategoryDrinksView(generics.ListAPIView):
    """Класс для отображения всех напитков определенной категории типа напитков"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = DrinksSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        # Получили список всех активных напитков по заданной категории типа напитков
        category_slug = self.kwargs["variety_in_drink_category_slug"]
        category = get_object_or_404(VarietyInDrinkCategory, slug=category_slug)
        drinks = category.drinks_set.filter(
            is_active=True
        ).all()

        return drinks


class GetCategoryVarietyInDrinkCategoryDrinksView(generics.ListAPIView):
    """Класс для отображения всех напитков определенной категории и определенной категории типа напитков"""

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = DrinksSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        # Получили список всех активных напитков по заданной категории и по заданной категории типа напитков
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(Category, slug=category_slug)
        category_varieties = category.varietyindrinkcategory_set.filter(
            is_active=True
        ).all()
        variety_in_drink_category_slug = self.kwargs["variety_in_drink_category_slug"]
        variety_in_drink_category = get_object_or_404(category_varieties, slug=variety_in_drink_category_slug)
        drinks = variety_in_drink_category.drinks_set.filter(
            is_active=True
        ).all()

        return drinks


class GetDrinksInfoFilterView(generics.ListAPIView):
    """Класс для фильтрации напитков по параметрам: Имя, Цена, Категория, Категория типа напитка"""

    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["name", "price", "category", "category_of_sort_drink"]


class GetDrinksInfoSearchView(generics.ListAPIView):
    """Класс для поиска напитков по параметрам: Имя напитка, Сокращенное имя напитка, Категория напитка, Категория
    типа напитка"""

    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.SearchFilter]
    search_fields = [
        "name",
        "slug",
        "category__name",
        "category_of_sort_drink__name",
    ]


class GetDrinksInfoOrderView(generics.ListAPIView):
    """Класс для упорядочивания поездок по параметрам: Направление, Дата, Время, Цена за место"""

    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ["name", "price"]
