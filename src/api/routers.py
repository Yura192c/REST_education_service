from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="HARDQODE EDUCATION API",
        default_version='v1.0.0',
        description=""
                    "You must be logged in to send some requests.",
        contact=openapi.Contact(name="Yra Mironchik",
                                url="https://t.me/murikoil",
                                email="yra.mironchik2003@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

DOCKS_urlpatterns = [

    # YASG documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

APPS_urlpatterns = [
    # API v1
    path('api/', include('src.api.urls')),

]

urlpatterns = DOCKS_urlpatterns + APPS_urlpatterns
