import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model=Tasks
        fields='__all__'




