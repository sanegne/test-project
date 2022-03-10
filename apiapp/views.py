from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filtersets import OrFilter, AndFilter
from .serializers import BookSerializer
from .models import Book


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    """
    BookAPI that can list, create, update, delete book on database.
    List function has the filterable, paginatable feature.
    Also search the book by text on synopsis, name, author field.
    """
    queryset = Book.objects
    serializer_class = BookSerializer
    filterset_fields = ['genere']
    filterset_class = OrFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['author', 'name', 'synopsis']

    def get_queryset(self):
        """
        operation: 'or'|'and'
        """
        operation = self.request.query_params.get('operation', 'or')
        if operation =='and':
            self.filterset_class = AndFilter
        return super().get_queryset()
