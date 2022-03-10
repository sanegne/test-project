from django.db.models import fields
from rest_framework import serializers
from .models import Book, GenreType


class BookSerializer(serializers.ModelSerializer):
    genere = serializers.ListField(
        child=serializers.ChoiceField(
            choices=GenreType.choices,
            allow_blank=False),
        write_only=True,
    )
    genere_types = serializers.CharField(source="genere", read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'