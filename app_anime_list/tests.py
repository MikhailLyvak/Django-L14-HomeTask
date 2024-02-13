from django.test import TestCase
from django.urls import reverse
from .models import Anime, AnimeType


class AnimeListTests(TestCase):
    def setUp(self):
        anime_type = AnimeType.objects.create(name='Action')
        Anime.objects.create(name='Naruto', description='An awesome anime', episodes=220, my_episode=150,
                             my_rating=9, type=anime_type)

    def test_index_view(self):
        response = self.client.get(reverse('app_anime_list:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мій список аніме на перегляд налічує:')
        self.assertContains(response, 'Мій список аніме налічє:')
        self.assertContains(response, 'Ви відвідали цей сайт')

    def test_anime_list_view(self):
        response = self.client.get(reverse('app_anime_list:anime-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Description')
        self.assertContains(response, 'Episodes')
        self.assertContains(response, 'My Rating')
        self.assertContains(response, 'Anime Type')
        self.assertContains(response, 'Naruto')
        self.assertContains(response, 'An awesome anime')
        self.assertContains(response, '150 / 220')
        self.assertContains(response, '9')
        self.assertContains(response, 'Action')

    def test_anime_model(self):
        anime = Anime.objects.get(name='Naruto')
        self.assertEqual(anime.description, 'An awesome anime')
        self.assertEqual(anime.episodes, 220)
        self.assertEqual(anime.my_episode, 150)
        self.assertEqual(anime.my_rating, 9)
        self.assertEqual(anime.type.name, 'Action')
        
    def test_anime_description_view(self):
        anime_with_description = Anime.objects.create(
            name='Anime With Description',
            description='This anime has a description',
            episodes=12,
            my_episode=12,
            my_rating=8.5,
            type=AnimeType.objects.create(name='Action')
        )

        anime_without_description = Anime.objects.create(
            name='Anime Without Description',
            episodes=24,
            my_episode=24,
            my_rating=7.8,
            type=AnimeType.objects.create(name='Adventure')
        )

        response = self.client.get(reverse('app_anime_list:anime-list'))
        self.assertContains(response, 'This anime has a description')

        self.assertContains(response, '-==-')
