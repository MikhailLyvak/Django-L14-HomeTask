from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Anime, AnimeType

def index(request):
    num_anime_types = AnimeType.objects.count()
    num_anime = Anime.objects.count()

    num_visits = request.session.get("num_visits", 0) 
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_anime": num_anime,
        "num_anime_types": num_anime_types,
        "num_visits": num_visits + 1
    }

    return render(request, "app_anime_list/index.html", context=context)


class AnimeListView(generic.ListView):
    model = Anime
    template_name = "app_anime_list/anime_list.html"
    context_object_name = "anime_list"
    
    def get_queryset(self):
        queryset = Anime.objects.select_related('type')
        return queryset 
    
class ItemCreateView(generic.CreateView):
    model = Anime
    template_name = "app_anime_list/create_item.html"
    fields = '__all__'
    success_url = reverse_lazy("app_anime_list:anime_list")
    
class TypeCreateView(generic.CreateView):
    model = AnimeType
    template_name = "app_anime_list/create_type.html"
    fields = "__all__"
    success_url = reverse_lazy("app_anime_list:anime_list")