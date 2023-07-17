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


class DrinkCategory(ShopInfoMixin):
    """Класс для создания модели - Категория Напитка"""

    image = models.FileField(upload_to="api/", default='api/coffee.webp')

    class Meta:
        verbose_name = "Drink Category"
        verbose_name_plural = "Drink Categories"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"


class VarietyInDrinkCategory(ShopInfoMixin):
    """Класс для создания модели - Разновидность кофе/чая/ ... """

    category = models.ForeignKey(
        DrinkCategory, verbose_name="Drink Category", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Variety In Drink Category"
        verbose_name_plural = "Varieties In Drink Category"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"


class Drinks(ShopInfoMixin):
    """Класс для создания модели - Напитки"""

    category = models.ForeignKey(
        DrinkCategory, verbose_name="Drink Category", on_delete=models.CASCADE
    )
    category_of_sort_drink = models.ForeignKey(
        VarietyInDrinkCategory, verbose_name="Variety In Drink Category", on_delete=models.CASCADE, null=True,
        blank=True
    )
    description = models.TextField(max_length=500, verbose_name="description")
    price = models.FloatField(
        default=0, validators=[MinValueValidator(1)], verbose_name="Price per drink"
    )
    image = models.FileField(upload_to="api/", default='api/coffee.webp')
    number_of_drink_glass_sizes = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(6)], verbose_name="Number of drink glass sizes"
    )

    class Meta:
        verbose_name = "Drinks"
        verbose_name_plural = "Drinks"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"


class FoodCategory(ShopInfoMixin):
    """Класс для создания модели - Категория Еды"""

    image = models.FileField(upload_to="api/",  default='api/food.jpg')

    class Meta:
        verbose_name = "Food Category"
        verbose_name_plural = "Food Categories"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"


class VarietyInFoodCategory(ShopInfoMixin):
    """Класс для создания модели - Разновидность завтраков/обедов ... """

    category = models.ForeignKey(
        FoodCategory, verbose_name="Food Category", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Variety In Food Category"
        verbose_name_plural = "Varieties In Food Category"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"


class Food(ShopInfoMixin):
    """Класс для создания модели - Еда"""

    category = models.ForeignKey(
        FoodCategory, verbose_name="Food Category", on_delete=models.CASCADE
    )
    category_of_sort_food = models.ForeignKey(
        VarietyInFoodCategory, verbose_name="Variety In Food Category", on_delete=models.CASCADE, null=True,
        blank=True
    )
    description = models.TextField(max_length=500, verbose_name="description")
    price = models.FloatField(
        default=0, validators=[MinValueValidator(1)], verbose_name="Price per food"
    )
    image = models.FileField(upload_to="api/",  default='api/food.jpg')

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Food products"

    def __str__(self) -> str:
        """Возвращает удобочитаемую строку для каждого объекта."""

        return f"{self.name}"
