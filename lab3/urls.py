from django.contrib import admin
from django.urls import path, include
from movies import views
from movies.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', views.index),
    path('films/<int:id>/', views.GetFilm, name='films_url'),
    path('seat/<int:id>/', views.GetSeat, name='seats_url'),
    path('seats/<int:id>/', views.MakeOrder, name='order_url'),
]
