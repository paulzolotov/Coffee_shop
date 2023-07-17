from .models import DrinkCategory, Drinks, VarietyInDrinkCategory, FoodCategory, Food, VarietyInFoodCategory
from rest_framework import serializers


class DrinkCategorySerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели DrinkCategory"""

    # ModelSerializer автоматически сгенерирует набор полей для вас, основываясь на модели.
    # Автоматически сгенерирует валидаторы для сериализатора, такие как unique_together валидаторы.
    # Включает в себя реализацию по умолчанию .create() и .update().
    class Meta:
        model = DrinkCategory
        fields = (
            "id",
            "name",
            "slug",
            "is_active",
            "image"
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


class FoodCategorySerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели FoodCategory"""

    class Meta:
        model = FoodCategory
        fields = (
            "id",
            "name",
            "slug",
            "is_active",
            "image"
        )


class VarietyInFoodCategorySerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели VarietyInFoodCategory"""

    class Meta:
        model = VarietyInFoodCategory
        fields = (
            "id",
            "name",
            "slug",
            "is_active"
        )


class FoodSerializer(serializers.ModelSerializer):
    """Класс, формирующий сериализованные данные модели Food"""

    class Meta:
        model = Food
        fields = (
            "id",
            "name",
            "slug",
            "is_active",
            "category",
            "category_of_sort_food",
            "description",
            "price",
            "image",
        )
