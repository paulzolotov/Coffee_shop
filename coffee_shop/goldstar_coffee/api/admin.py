from django.contrib import admin
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Category, Drinks, VarietyInDrinkCategory

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


@admin.register(Category)
class CategoryAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о категории напитка."""

    list_display = (
        "name",
        "is_active",
        "slug",
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
            + urlencode({"departure_category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Drinks</a>', url, count)


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
            + urlencode({"departure_category_of_sort_drink_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Drinks</a>', url, count)


@admin.register(Drinks)
class DrinksAdmin(FunctionsForActions):
    """Класс для отображения на панели администратора информации о напитках."""

    list_display = (
        "name",
        "is_active",
        "slug",
        "image",
        "category",
        "category_of_sort_drink",
        "price",
        "description",
    )

    sortable_by = ("name", "price", "category", "category_of_sort_drink")
    list_filter = ("name", "price", "category", "category_of_sort_drink")
    actions = ("make_inactive", "make_active")

    @admin.display(description="custom price")
    def show_pretty_price(self, obj) -> str:
        """Функция для отображения кастомной записи для 'цены за место' (В данном случае добавили знак $)"""

        return f"{obj.price} BYN"
