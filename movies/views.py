from django.shortcuts import render
from datetime import date
from rest_framework import viewsets
from .models import Films, Seats, Users
from .serializers import FilmsSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = FilmsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = FilmsSerializer


def index(request):
    return render(request, 'films.html', {'data' : {
        'current_date': date.today(),
        'films': Films.objects.all()
    }})


def GetFilm(request, id):
    return render(request, 'film.html', {'data' : {
        'current_date': date.today(),
        'film': Films.objects.filter(id=id)[0]
    }})
