from django.contrib import admin

from .models import Anime, AnimeType


class AnimeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class AnimeAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'my_rating', 'type', 'my_episode', 'episodes')
    list_filter = ('my_rating', 'type', 'my_episode', 'episodes')


admin.site.register(Anime, AnimeAdmin)
admin.site.register(AnimeType, AnimeTypeAdmin)
