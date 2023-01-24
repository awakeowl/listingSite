from django.contrib import admin
from django.urls import path, re_path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Solai",
        default_version='v2',
        description="Rentscore listing site",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@renscore.africa"),
        # license=openapi.License(name="MIT"),
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls'), name='accounts'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc',
                                 cache_timeout=10), name='schema-redoc'),
]
