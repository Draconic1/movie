from django.shortcuts import render
from datetime import date
from rest_framework import viewsets

from .models import Films, Seats, Users, Orders
from .serializers import FilmsSerializer, SeatsSerializer, UsersSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


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


def GetSeat(request, id):
    return render(request, 'seat.html', {'data' : {
        'current_date': date.today(),
        'film': Films.objects.filter(id=id)[0],
        'seat': Seats.objects.all(),
        'user': Users.objects.all(),
        'order': Orders.objects.all()
    }})


def MakeOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'seat': Seats.objects.filter(id=id)[0],
        'user': Users.objects.all(),
        'order': Orders.objects.all()
    }})
