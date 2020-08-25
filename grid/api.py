from .models import Grid, GridElement
from rest_framework import viewsets, serializers, permissions


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = ["id", "name"]


class GridElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = GridElement
        fields = ["id", "grid", "uid"]

    def validate(self, attrs):
        # Only allow an element to be added to a grid
        # owned by the current user.
        user = self.context["request"].user
        if attrs["grid"].user == user:
            return attrs
        raise serializers.ValidationError


class GridViewSet(viewsets.ModelViewSet):
    queryset = Grid.objects.all()
    serializer_class = GridSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Override so we can set the user on save
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Limit the scope to the current user
        query = super().get_queryset()
        return query.filter(user=self.request.user)


class GridElementViewSet(viewsets.ModelViewSet):
    queryset = GridElement.objects.all()
    serializer_class = GridElementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Limit the scope to the current user
        query = super().get_queryset()
        return query.filter(grid__user=self.request.user)
