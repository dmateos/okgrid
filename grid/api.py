from .models import Grid, GridElement
from rest_framework import viewsets, permissions, serializers


class GridSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grid
        fields = ["id", "name"]


class GridElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GridElement
        fields = ["id", "grid", "uid"]


class GridViewSet(viewsets.ModelViewSet):
    queryset = Grid.objects.all()
    serializer_class = GridSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(user=self.request.user)


class GridElementViewSet(viewsets.ModelViewSet):
    queryset = GridElement.objects.all()
    serializer_class = GridElementSerializer
    permission_classes = [permissions.IsAuthenticated]
