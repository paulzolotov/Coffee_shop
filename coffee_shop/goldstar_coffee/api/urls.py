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
    path("categories/", views.GetCategoryInfoView.as_view()),
    path("drink-categories/", views.GetVarietyInDrinkCategoryInfoView.as_view()),
    path("drinks/", views.GetDrinksInfoView.as_view()),
    path(
        "category/<slug:category_slug>/",
        views.GetCategoryDrinksView.as_view(),
    ),
    path(
        "variety/<slug:variety_in_drink_category_slug>/",
        views.GetVarietyInDrinkCategoryDrinksView.as_view(),
    ),
    path(
        "category-variety/<slug:category_slug>/<slug:variety_in_drink_category_slug>/",
        views.GetCategoryVarietyInDrinkCategoryDrinksView.as_view(),
    ),
    path("filter-drinks/", views.GetDrinksInfoFilterView.as_view()),
    path("search-drinks/", views.GetDrinksInfoSearchView.as_view()),
    path("order-drinks/", views.GetDrinksInfoOrderView.as_view()),
]
