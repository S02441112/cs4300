from django.test import TestCase
from .models import Movie

class MovieTestCase(TestCase):
    def test_movie_creation(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="Cool description",
            release_date="1998-01-01",
            duration=120
        )
        self.assertEqual(movie.title, "Test Movie")
