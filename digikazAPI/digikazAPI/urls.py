from django.contrib import admin
from django.urls import include, path

from users import views as users_views

from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Digikaz API",
        default_version='v1',
    ),
    public=True
)


router = DefaultRouter()
router.register(r'users', users_views.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
