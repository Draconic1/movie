from movies.models import Films, Users, Seats
from rest_framework import serializers


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = "__all__"