from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class ShopInfoMixin(models.Model):
    """Класс Mixin, для повторяющихся полей, от которого затем наследуются классы с моделями"""

    slug = models.SlugField(max_length=70, verbose_name="Short Name")
    name = models.CharField(max_length=70, verbose_name="Name")
    is_active = models.BooleanField(default=True, verbose_name="Is it active?")

    class Meta:
        abstract = True


class Category(ShopInfoMixin):
    """Класс для создания модели - Категория Напитка"""

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"


class VarietyInDrinkCategory(ShopInfoMixin):
    """Класс для создания модели - Разновидность кофе/чая/ ... """

    category = models.ForeignKey(
        Category, verbose_name="Drink Category", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Variety"
        verbose_name_plural = "Varieties"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"


class Drinks(ShopInfoMixin):
    """Класс для создания модели - Напитки"""

    category = models.ForeignKey(
        Category, verbose_name="Drink Category", on_delete=models.CASCADE
    )
    category_of_sort_drink = models.ForeignKey(
        VarietyInDrinkCategory, verbose_name="Variety In Drink Category", on_delete=models.CASCADE
    )
    description = models.TextField(max_length=500, verbose_name="description")
    price = models.IntegerField(
        default=0, validators=[MinValueValidator(1)], verbose_name="Price per drink"
    )
    image = models.FileField(upload_to="api/")
    number_of_drink_glass_sizes = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(6)], verbose_name="Number of drink glass sizes"
    )

    class Meta:
        verbose_name = "Drinks"
        verbose_name_plural = "Drinks"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"