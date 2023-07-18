from .models import DrinkCategory, Drinks, VarietyInDrinkCategory, FoodCategory, Food, VarietyInFoodCategory
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters
from rest_framework import generics
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (DrinkCategorySerializer, VarietyInDrinkCategorySerializer,
                          DrinksSerializer, FoodSerializer, VarietyInFoodCategorySerializer, FoodCategorySerializer)


class GetDrinkCategoryInfoView(APIView):
    """Класс для отображения всех активных категорий напитков"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся Категорий напитков"""

        queryset = DrinkCategory.objects.filter(is_active=True).all()
        serializer_for_queryset = DrinkCategorySerializer(instance=queryset, many=True)
        return Response({"categories": serializer_for_queryset.data})


class GetVarietyInDrinkCategoryInfoView(APIView):
    """Класс для отображения всех активных типов напитков во всех категориях напитков"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся типов напитков во всех категориях напитков"""

        queryset = VarietyInDrinkCategory.objects.filter(is_active=True).all()
        serializer_for_queryset = VarietyInDrinkCategorySerializer(instance=queryset, many=True)
        return Response({"variety_in_drink_category": serializer_for_queryset.data})


class GetDrinksInfoView(APIView):
    """Класс для отображения всех активных напитков"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся Напитков"""

        queryset = Drinks.objects.filter(is_active=True).all()
        serializer_for_queryset = DrinksSerializer(instance=queryset, many=True)
        return Response({"drinks": serializer_for_queryset.data})


class GetDrinksFromCategoryView(generics.ListAPIView):
    """Класс для отображения всех напитков определенной категории"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = DrinksSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        # Получили список всех активных напитков по заданной категории
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(DrinkCategory, slug=category_slug)
        drinks = category.drinks_set.filter(
            is_active=True
        ).all()

        return drinks


class GetDrinksFromVarietyView(generics.ListAPIView):
    """Класс для отображения всех напитков определенной категории типа напитков"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
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


class GetVarietiesFromDrinkCategoryView(generics.ListAPIView):
    """Класс для отображения типов напитков определенной категории"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = VarietyInDrinkCategorySerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        # Получили список всех активных напитков по заданной категории
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(DrinkCategory, slug=category_slug)
        varieties = category.varietyindrinkcategory_set.filter(
            is_active=True
        ).all()

        return varieties


class GetDrinksFromVarietyInCategoryView(generics.ListAPIView):
    """Класс для отображения всех напитков определенной категории и определенной категории типа напитков"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = DrinksSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        # Получили список всех активных напитков по заданной категории и по заданной категории типа напитков
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(DrinkCategory, slug=category_slug)
        category_varieties = category.varietyindrinkcategory_set.filter(
            is_active=True
        ).all()
        variety_in_drink_category_slug = self.kwargs["variety_in_drink_category_slug"]
        variety_in_drink_category = get_object_or_404(category_varieties, slug=variety_in_drink_category_slug)
        drinks = variety_in_drink_category.drinks_set.filter(
            is_active=True
        ).all()

        return drinks


class GetOneDrinkFromCategoryView(generics.ListAPIView):
    """Класс для отображения определенного напитка определенной категории"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = DrinksSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        drink_id = self.kwargs["id"]
        drink = Drinks.objects.filter(id=drink_id)

        return drink


class GetDrinksInfoFilterView(generics.ListAPIView):
    """Класс для фильтрации напитков по параметрам: Имя, Цена, Категория, Категория типа напитка"""

    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["name", "price", "category", "category_of_sort_drink"]


class GetDrinksInfoSearchView(generics.ListAPIView):
    """Класс для поиска напитков по параметрам: Имя напитка, Сокращенное имя напитка, Категория напитка, Категория
    типа напитка"""

    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.SearchFilter]
    search_fields = [
        "name",
        "slug",
        "category__name",
        "category_of_sort_drink__name",
    ]


class GetDrinksInfoOrderView(generics.ListAPIView):
    """Класс для упорядочивания напитков по параметрам: Имя, Цена за напиток"""

    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer
    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ["name", "price"]


class GetFoodCategoryInfoView(APIView):
    """Класс для отображения всех активных категорий еды"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся Категорий еды"""

        queryset = FoodCategory.objects.filter(is_active=True).all()
        serializer_for_queryset = FoodCategorySerializer(instance=queryset, many=True)
        return Response({"categories": serializer_for_queryset.data})


class GetVarietyInFoodCategoryInfoView(APIView):
    """Класс для отображения всех активных типов еды во всех категориях еды"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся типов еды во всех категориях еды"""

        queryset = VarietyInFoodCategory.objects.filter(is_active=True).all()
        serializer_for_queryset = VarietyInFoodCategorySerializer(instance=queryset, many=True)
        return Response({"variety_in_food_category": serializer_for_queryset.data})


class GetFoodProductsInfoView(APIView):
    """Класс для отображения всех активных продуктов еды"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request: Request) -> Response:
        """Получили сериализованные данные имеющихся продуктов еды"""

        queryset = Food.objects.filter(is_active=True).all()
        serializer_for_queryset = FoodSerializer(instance=queryset, many=True)
        return Response({"food": serializer_for_queryset.data})


class GetFoodProductsFromCategoryView(generics.ListAPIView):
    """Класс для отображения всех продуктов еды определенной категории"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = FoodSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные продуктов еды"""

        # Получили список всех активных продуктов еды по заданной категории
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(FoodCategory, slug=category_slug)
        food = category.food_set.filter(
            is_active=True
        ).all()

        return food


class GetFoodProductsFromVarietyView(generics.ListAPIView):
    """Класс для отображения всех продуктов еды определенной категории типа еды"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = FoodSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные продуктов еды"""

        # Получили список всех активных продуктов еды по заданной категории типа еды
        category_slug = self.kwargs["variety_in_food_category_slug"]
        category = get_object_or_404(VarietyInFoodCategory, slug=category_slug)
        food = category.food_set.filter(
            is_active=True
        ).all()

        return food


class GetVarietiesFromFoodCategoryView(generics.ListAPIView):
    """Класс для отображения типов напитков определенной категории"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = VarietyInFoodCategorySerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        # Получили список всех активных напитков по заданной категории
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(FoodCategory, slug=category_slug)
        varieties = category.varietyinfoodcategory_set.filter(
            is_active=True
        ).all()

        return varieties


class GetFoodProductsFromVarietyInCategoryView(generics.ListAPIView):
    """Класс для отображения всех продуктов еды определенной категории и определенной категории типа еды"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = FoodSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные всех продуктов еды"""

        # Получили список всех активных продуктов еды по заданной категории и по заданной категории типа еды
        category_slug = self.kwargs["category_slug"]
        category = get_object_or_404(FoodCategory, slug=category_slug)
        category_varieties = category.varietyinfoodcategory_set.filter(
            is_active=True
        ).all()
        variety_in_food_category_slug = self.kwargs["variety_in_food_category_slug"]
        variety_in_food_category = get_object_or_404(category_varieties, slug=variety_in_food_category_slug)
        food = variety_in_food_category.food_set.filter(
            is_active=True
        ).all()

        return food


class GetOneFoodProductFromCategoryView(generics.ListAPIView):
    """Класс для отображения определенного продукта еды определенной категории"""

    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = FoodSerializer

    def get_queryset(self) -> QuerySet:
        """Получили сериализованные данные напитков"""

        food_pr_id = self.kwargs["id"]
        food_pr = Food.objects.filter(id=food_pr_id)

        return food_pr


class GetFoodProductsInfoFilterView(generics.ListAPIView):
    """Класс для фильтрации напитков по параметрам: Имя, Цена, Категория, Категория типа еды"""

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["name", "price", "category", "category_of_sort_food"]


class GetFoodProductsInfoSearchView(generics.ListAPIView):
    """Класс для поиска продуктов еды по параметрам: Имя еды, Сокращенное имя еды, Категория еды, Категория
    типа еды"""

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.SearchFilter]
    search_fields = [
        "name",
        "slug",
        "category__name",
        "category_of_sort_food__name",
    ]


class GetFoodProductsInfoOrderView(generics.ListAPIView):
    """Класс для упорядочивания продуктов еды по параметрам: Имя, Цена за продукт"""

    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ["name", "price"]
