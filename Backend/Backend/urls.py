
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from productos.views import ChelaViewSet

router = DefaultRouter()
router.register(r'productos', ChelaViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('admin/', admin.site.urls),
]
