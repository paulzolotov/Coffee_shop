from django.urls import path, re_path

from . import views


urlpatterns = [
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
