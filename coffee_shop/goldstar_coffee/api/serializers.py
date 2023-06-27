from .models import Category, Drinks, VarietyInDrinkCategory
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели Category"""

    # ModelSerializer автоматически сгенерирует набор полей для вас, основываясь на модели.
    # Автоматически сгенерирует валидаторы для сериализатора, такие как unique_together валидаторы.
    # Включает в себя реализацию по умолчанию .create() и .update().
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
            "is_active"
        )


class VarietyInDrinkCategorySerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели VarietyInDrinkCategory"""

    class Meta:
        model = VarietyInDrinkCategory
        fields = (
            "id",
            "name",
            "slug",
            "is_active"
        )


class DrinksSerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели Drinks"""

    class Meta:
        model = Drinks
        fields = (
            "id",
            "name",
            "slug",
            "is_active",
            "category",
            "category_of_sort_drink",
            "description",
            "price",
            "image",
            "number_of_drink_glass_sizes"
        )
