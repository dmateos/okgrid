from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import grid.api as api
import grid.views as views

router = routers.DefaultRouter()
router.register(r"grids", api.GridViewSet)
router.register(r"gridelements", api.GridElementViewSet)

urlpatterns = [
    path('grids/', views.GridListView.as_view(), name="grids"),
    path('grids/<int:pk>', views.GridDetailView.as_view(), name="griddetails"),

    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.root, name="index"),
]
