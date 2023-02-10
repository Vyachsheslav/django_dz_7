from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.Permissions import IsOwnerPermission
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator', 'status', 'created_at']

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        
    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["update", "destroy", "partial_update"]:
            return [IsOwnerPermission()]
        return []
