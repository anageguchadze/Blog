from django_filters import rest_framework as filters
from .models import Blog


class BlogFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')
    created_at = filter.DateFromToRangeFilter()

    class meta:
        model = Blog
        fields = '__all__'