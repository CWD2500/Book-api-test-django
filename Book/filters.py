import django_filters
from .models import Book




class BookFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    price = django_filters.filters.CharFilter(field_name='price' or 0 , lookup_expr='gte' )
    description = django_filters.filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('name' , 'price' , 'description')