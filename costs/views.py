from rest_framework.viewsets import ModelViewSet
from .models import DailyCosts
from .serializers import DailyCostsSerializer
from .permissions import CustomPermission


class DailyCostsAPIView(ModelViewSet):
    queryset = DailyCosts.objects.all()
    serializer_class = DailyCostsSerializer
    permission_classes = [CustomPermission]