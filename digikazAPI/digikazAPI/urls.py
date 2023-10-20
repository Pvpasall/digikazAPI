from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users import views as users_views

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
