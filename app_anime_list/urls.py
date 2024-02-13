from django.urls import path, include


from .views import (
    index,
    AnimeListView,
    ItemCreateView,
    TypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("anime_list", AnimeListView.as_view(), name="anime_list"),
    path("anime_list/create", ItemCreateView.as_view(), name="create_anime"),
    path("anime_list/create_type", TypeCreateView.as_view(), name="create_type"),
 
]

app_name = "app_anime_list"