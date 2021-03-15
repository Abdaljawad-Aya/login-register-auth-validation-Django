import django_filters
from django_filters import DateFilter, CharFilter


from .models import * 

class OrderFilters(django_filters.FilterSet)