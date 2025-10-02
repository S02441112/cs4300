from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView



class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'description', 'release_date', 'duration']  
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie_list')  # redirect after saving

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

# Movie CRUD
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

# Seat availability and booking
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally filter seats by movie_id query parameter:
        /api/seats/?movie_id=1
        """
        queryset = super().get_queryset()
        movie_id = self.request.query_params.get('movie_id')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset

    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        seat = self.get_object()
        if seat.is_booked:
            return Response({"error": "Seat already booked"}, status=status.HTTP_400_BAD_REQUEST)
        seat.is_booked = True
        seat.save()

        # Create Booking for the correct movie
        movie_id = request.data.get('movie_id') or seat.movie.id
        Booking.objects.create(
            movie_id=movie_id,
            seat=seat,
            user=None
        )
        return Response({
            "success": f"Seat {seat.seat_number} for movie ID {movie_id} booked successfully"
        })


# Booking CRUD
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        Optionally filter bookings by movie_id query parameter:
        /api/bookings/?movie_id=1
        """
        queryset = super().get_queryset()
        movie_id = self.request.query_params.get('movie_id')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=None)  # no login required

# Template views
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)  # Only seats for this movie
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id)
        if not seat.is_booked:
            seat.is_booked = True
            seat.save()
            Booking.objects.create(movie=movie, seat=seat, user=None)
        return redirect('booking_history')
        
    return render(request, 'seat_booking.html', {'movie': movie, 'seats': seats})


def booking_history(request):
    bookings = Booking.objects.all()  # show all bookings since no user
    return render(request, 'booking_history.html', {'bookings': bookings})
