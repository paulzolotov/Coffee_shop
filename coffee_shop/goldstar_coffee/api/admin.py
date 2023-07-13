from django.contrib import admin
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html, mark_safe
from django.utils.http import urlencode

from .models import DrinkCategory, Drinks, VarietyInDrinkCategory, FoodCategory, Food, VarietyInFoodCategory

# Register your models here.


class FunctionsForActions(admin.ModelAdmin):
    """Класс для повторяющихся функций для всех классов отображения"""

    @admin.action(description="Перевести в неактивное состояние")
    def make_inactive(self, request: HttpRequest, queryset) -> None:
        """Функция для перевода в строке 'action' в состояние 'inactive'"""

        queryset.update(is_active=False)

    @admin.action(description="Перевести в активное состояние")
    def make_active(self, request: HttpRequest, queryset) -> None:
        """Функция для перевода в строке 'action' в состояние 'active'"""

        queryset.update(is_active=True)


@admin.register(DrinkCategory)
class DrinkCategoryAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о категории напитка."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "view_drinks_link",
        "view_varieties_link"
    )

    actions = ("make_inactive", "make_active")

    @admin.display(description="drinks")
    def view_drinks_link(self, obj):
        """Функция для подсчета количества напитков определенной категории, а также генерации ссылки
        на эти напитки"""

        count = obj.drinks_set.count()
        url = (
            reverse("admin:api_drinks_changelist")
            + "?"
            + urlencode({"category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Drinks</a>', url, count)

    @admin.display(description="varieties")
    def view_varieties_link(self, obj):
        """Функция для подсчета количества разнообразных вариантов напитков определенной категории, а также генерации
        ссылки на эти варианты"""

        count = obj.varietyindrinkcategory_set.count()
        url = (
            reverse("admin:api_varietyindrinkcategory_changelist")
            + "?"
            + urlencode({"category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Varieties</a>', url, count)


@admin.register(VarietyInDrinkCategory)
class VarietyInDrinkCategoryAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о разнообразии определенного напитка в категории."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "category",
        "view_drinks_link"
    )

    actions = ("make_inactive", "make_active")

    @admin.display(description="drinks")
    def view_drinks_link(self, obj):
        """Функция для подсчета количества напитков определенной категории, а также генерации ссылки
        на эти напитки"""

        count = obj.drinks_set.count()
        url = (
            reverse("admin:api_drinks_changelist")
            + "?"
            + urlencode({"category_of_sort_drink_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Drinks</a>', url, count)


@admin.register(Drinks)
class DrinksAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о напитках."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "img_preview",
        "category",
        "category_of_sort_drink",
        "price",
        "description",
        "number_of_drink_glass_sizes"
    )

    sortable_by = ("name", "price", "category", "category_of_sort_drink")
    list_filter = ("price", "category", "category_of_sort_drink")
    actions = ("make_inactive", "make_active")
    readonly_fields = ("img_tag",)

    @admin.display(description="custom price")
    def show_pretty_price(self, obj) -> str:
        """Функция для отображения кастомной записи для 'цены за напиток' (В данном случае добавили знак $)"""

        return f"{obj.price} $"

    @admin.display(description="drink image")
    def img_preview(self, obj):
        """Функция для отображения иконки с напитком определенного размера"""

        return mark_safe(
            f'<img src = "{obj.image.url}" width = "70px" height="90px"/>'
        )

    @admin.display(description="image tag")
    def img_tag(self, obj):
        """Функция для отображения иконки с напитком определенного размера"""

        return mark_safe(
            f'<img src = "{obj.image.url}" width = "70px" height="90px"/>'
        )


@admin.register(FoodCategory)
class FoodCategoryAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о категории еды."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "view_food_link"
    )

    actions = ("make_inactive", "make_active")

    @admin.display(description="Food Products")
    def view_food_link(self, obj):
        """Функция для подсчета количества продуктов еды определенной категории, а также генерации ссылки
        на эти продукты"""

        count = obj.food_set.count()
        url = (
            reverse("admin:api_food_changelist")
            + "?"
            + urlencode({"category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Food Products</a>', url, count)

    @admin.display(description="varieties")
    def view_varieties_link(self, obj):
        """Функция для подсчета количества разнообразных вариантов еды определенной категории, а также генерации
        ссылки на эти варианты"""

        count = obj.varietyinfoodcategory_set.count()
        url = (
            reverse("admin:api_varietyinfoodcategory_set_changelist")
            + "?"
            + urlencode({"category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Varieties</a>', url, count)


@admin.register(VarietyInFoodCategory)
class VarietyInFoodCategoryAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о разнообразии определенного еды в категории."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "category",
        "view_food_link"
    )

    actions = ("make_inactive", "make_active")

    @admin.display(description="Food products")
    def view_food_link(self, obj):
        """Функция для подсчета количества продуктов еды определенной категории, а также генерации ссылки
        на эти продукты"""

        count = obj.food_set.count()
        url = (
            reverse("admin:api_food_changelist")
            + "?"
            + urlencode({"category_of_sort_food_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Food Products</a>', url, count)


@admin.register(Food)
class FoodAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о продуктах еды."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "img_preview",
        "category",
        "category_of_sort_food",
        "price",
        "description",
    )

    sortable_by = ("name", "price", "category", "category_of_sort_food")
    list_filter = ("price", "category", "category_of_sort_food")
    actions = ("make_inactive", "make_active")
    readonly_fields = ("img_tag",)

    @admin.display(description="custom price")
    def show_pretty_price(self, obj) -> str:
        """Функция для отображения кастомной записи для 'цены за продукт еды' (В данном случае добавили знак $)"""

        return f"{obj.price} $"

    @admin.display(description="drink image")
    def img_preview(self, obj):
        """Функция для отображения иконки с продуктом еды определенного размера"""

        return mark_safe(
            f'<img src = "{obj.image.url}" width = "70px" height="90px"/>'
        )

    @admin.display(description="image tag")
    def img_tag(self, obj):
        """Функция для отображения иконки с продуктом еды определенного размера"""

        return mark_safe(
            f'<img src = "{obj.image.url}" width = "70px" height="90px"/>'
        )
