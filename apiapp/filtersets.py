import django_filters
from .models import Book, GenreType


class AndFilter(django_filters.FilterSet):
    """
    Filter by genere field with AND operation.
    """
    genere = django_filters.MultipleChoiceFilter(choices=GenreType.choices, lookup_expr="contains", conjoined=True)
    
    class Meta:
        model = Book
        fields = ['genere']


class OrFilter(django_filters.FilterSet):
    """
    Filter by genere field with OR operation.
    """
    genere = django_filters.MultipleChoiceFilter(choices=GenreType.choices, lookup_expr="contains")
    
    class Meta:
        model = Book
        fields = ['genere']


