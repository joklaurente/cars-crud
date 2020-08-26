import django_filters
from .models import Car

class CarFiler(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            'color': ['exact'],
            }