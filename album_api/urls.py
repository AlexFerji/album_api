from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from music.views import AlbumListCreate, ArtistListCreate, TrackListCreate
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Album API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = SimpleRouter()
router.register('artist', ArtistListCreate, basename='artist')
router.register('track', TrackListCreate, basename='track')
router.register('album', AlbumListCreate, basename='album')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router.urls) ),
    path('api/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
