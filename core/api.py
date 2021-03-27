from core.models import People
from core.serializers import PeopleSerializer
from rest_framework import generics
from rest_framework import permissions


class PeopleList(generics.ListCreateAPIView):
    queryset = People.objects.filter()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.AllowAny]


class PeopleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.filter()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.AllowAny]
