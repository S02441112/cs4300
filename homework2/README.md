https://github.com/DevEdu-IO/docker-django/blob/master/README.md

# Running the Django Application


    python3 manage.py runserver 0.0.0.0:3000

Accessing The Rails Application

## Windows, MacOS, & Linux

    http://localhost:3000


Default page → should be movie list.
Click "Book Now" → navigates to seat booking with 15 available seats.
Click a seat → marking as booked and shows summary of bookings.

## Run tests
python3 manage.py test -v 2