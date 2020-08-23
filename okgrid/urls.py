from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import grid.api as api
import grid.views as views

router = routers.DefaultRouter()
router.register(r"grids", api.GridViewSet)
router.register(r"gridelements", api.GridElementViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.root),
]
