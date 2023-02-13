from django_filters import rest_framework as filters
from django_filters import rest_framework as filters, DateTimeFromToRangeFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateTimeFromToRangeFilter()
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ('created_at', 'status')
