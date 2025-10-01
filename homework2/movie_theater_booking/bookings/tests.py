from django.test import TestCase, Client
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Very Cool Mega Epic Movie",
            description="An Even Cooler Description",
            release_date="2525-10-01",
            duration=120
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Very Cool Mega Epic Movie")
        self.assertEqual(self.movie.description, "An Even Cooler Description")
        self.assertEqual(self.movie.release_date, "2525-10-01")
        self.assertEqual(self.movie.seats.count(), 15) # post save creates 15 seats upon movie creation

class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Very Cool Mega Epic Movie",
            description="An Even Cooler Description",
            release_date="2525-10-01",
            duration=120
        )
        # create 2 seats manually for testing
        self.seat1 = Seat.objects.create(movie=self.movie, seat_number="S01")
        self.seat2 = Seat.objects.create(movie=self.movie, seat_number="S02")

    def test_seat_creation(self):
        self.assertEqual(self.seat1.movie, self.movie)
        self.assertFalse(self.seat1.is_booked)

class BookingModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Very Cool Mega Epic Movie",
            description="An Even Cooler Description",
            release_date="2525-10-01",
            duration=120
        )
        self.seat = Seat.objects.create(movie=self.movie, seat_number="S01")
        self.booking = Booking.objects.create(movie=self.movie, seat=self.seat, user=None)

    def test_booking_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)

class SeatBookingIntegrationTest(TestCase):
    def setUp(self):
        # Create a test movie
        self.movie = Movie.objects.create(
            title="Integration Test Movie",
            description="Testing seat booking flow",
            release_date="2025-10-01",
            duration=120
        )
        # Create 3 seats for this movie
        self.seat1 = Seat.objects.create(movie=self.movie, seat_number="S01")
        self.seat2 = Seat.objects.create(movie=self.movie, seat_number="S02")
        self.seat3 = Seat.objects.create(movie=self.movie, seat_number="S03")
        
        # Initialize test client
        self.client = Client()

    def test_seat_booking_flow(self):
        # Step 1: Get seat booking page
        response = self.client.get(f'/movies/{self.movie.id}/seats/')
        self.assertEqual(response.status_code, 200)
        # Verify all seats are initially not booked
        for seat in [self.seat1, self.seat2, self.seat3]:
            self.assertFalse(seat.is_booked)

        # Step 2: Book seat1 via POST
        response = self.client.post(f'/movies/{self.movie.id}/seats/', {
            'seat_id': self.seat1.id
        })
        # After booking, should redirect
        self.assertEqual(response.status_code, 302)

        # Refresh seat from DB
        self.seat1.refresh_from_db()
        self.assertTrue(self.seat1.is_booked)

        # Step 3: Booking history page (optional)
        response = self.client.get('/bookings/history/')
        self.assertEqual(response.status_code, 200)
        # Ensure Booking exists
        booking_exists = Booking.objects.filter(seat=self.seat1, movie=self.movie).exists()
        self.assertTrue(booking_exists)