from core.models import People
from rest_framework import serializers


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = ['pk', "name", "email", "height", "weight", "imc"]
        read_only_fields = ["imc", ]
