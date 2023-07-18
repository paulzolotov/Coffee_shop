from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Coffee Shop API",
        default_version="v1",
        description="This api is developed primarily for the Coffee Shop and allows you to get information about "
                    "various drinks and food.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="saiwa@mail.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("drink-categories/", views.GetDrinkCategoryInfoView.as_view()),
    path("varieties-drink-categories/", views.GetVarietyInDrinkCategoryInfoView.as_view()),
    path("drinks/", views.GetDrinksInfoView.as_view()),
    path(
        "drinks-from-category/<slug:category_slug>/",
        views.GetDrinksFromCategoryView.as_view(),
    ),
    path(
        "varieties-from-drinkcategory/<slug:category_slug>/",
        views.GetVarietiesFromDrinkCategoryView.as_view(),
    ),
    path(
        "drinks-from-variety/<slug:variety_in_drink_category_slug>/",
        views.GetDrinksFromVarietyView.as_view(),
    ),
    path(
        "drink-category-variety/<slug:category_slug>/<slug:variety_in_drink_category_slug>/",
        views.GetDrinksFromVarietyInCategoryView.as_view(),
    ),
    path(
        "drinks-from-category/<slug:category_slug>/<int:id>/",
        views.GetOneDrinkFromCategoryView.as_view(),
    ),
    path("filter-drinks/", views.GetDrinksInfoFilterView.as_view()),
    path("search-drinks/", views.GetDrinksInfoSearchView.as_view()),
    path("order-drinks/", views.GetDrinksInfoOrderView.as_view()),
    path("food-categories/", views.GetFoodCategoryInfoView.as_view()),
    path("varieties-food-categories/", views.GetVarietyInFoodCategoryInfoView.as_view()),
    path("food/", views.GetFoodProductsInfoView.as_view()),
    path(
        "food-from-category/<slug:category_slug>/",
        views.GetFoodProductsFromCategoryView.as_view(),
    ),
    path(
        "varieties-from-foodcategory/<slug:category_slug>/",
        views.GetVarietiesFromFoodCategoryView.as_view(),
    ),
    path(
        "food-from-variety/<slug:variety_in_food_category_slug>/",
        views.GetFoodProductsFromVarietyView.as_view(),
    ),
    path(
        "food-category-variety/<slug:category_slug>/<slug:variety_in_food_category_slug>/",
        views.GetFoodProductsFromVarietyInCategoryView.as_view(),
    ),
    path(
        "food-from-category/<slug:category_slug>/<int:id>/",
        views.GetOneFoodProductFromCategoryView.as_view(),
    ),
    path("filter-food/", views.GetFoodProductsInfoFilterView.as_view()),
    path("search-food/", views.GetFoodProductsInfoSearchView.as_view()),
    path("order-food/", views.GetFoodProductsInfoOrderView.as_view()),
]
