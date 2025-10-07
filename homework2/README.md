# Self Hosted on Docker (Installation)
Project Self Hosted on Docker - not DevEdu
https://github.com/DevEdu-IO/docker-django/blob/master/README.md

# Setup Django Application
```
git clone https://github.com/S02441112/cs4300.git
cd ~/homework2/movie_theater_booking

python3 -m venv hw2_venv
source hw2_venv/bin/activate
```
## Install Dependencies 
```
pip install -r requirements.txt
```
## Migrate Database
```
python manage.py makemigrations
python manage.py migrate
```
## Run the Django Application
```
python3 manage.py runserver 0.0.0.0:3000
```
## Visit Application
```
http://localhost:3000
```
## Layout
Default page → list of movies.
Click "Book Now" → navigates to seat booking with 15 available seats.
Click a seat → marking as booked and shows summary of bookings.
Use /api tfor CRUD operations
## Run tests
```
python3 manage.py test -v 2
```
## Running the Django Application on the Web (Render Hosted)
```
    https://cs4300movie-app.onrender.com/
```
Able to perform CRUD operations on the api
```
    movies:     https://cs4300movie-app.onrender.com/api/movies/
    seats:      https://cs4300movie-app.onrender.com/api/seats/
    bookings:   https://cs4300movie-app.onrender.com/api/bookings/
```
Display data performed from CRUD operations by api on regular site (also added CRUD operations on regular site for implementation prctice)
Able to perform CRUD operations on the api
```
    movie list:     https://cs4300movie-app.onrender.com/
    movie seats:    https://cs4300movie-app.onrender.com/movies/<movie_id>/seats/
    delete movie:   https://cs4300movie-app.onrender.com/movies/<movie_id>/delete/
    add movie:      https://cs4300movie-app.onrender.com/add/
    booking list:   https://cs4300movie-app.onrender.com/bookings/history/
```
# AI Usage
Many aspects of the html files were provided via chat ChatGPT (GPT-5)
Troubleshooting deployment to render was heavily guided by GPT-5
Test cases inspired by GPT-5
