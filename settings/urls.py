"""
Mini-Gymi URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from helpers.health_check_view import health_check
from settings import settings


###
# Swagger
###
schema_v1_view = get_schema_view(
    openapi.Info(
        title="Mini-Gymi API",
        default_version='v1',
        description="Add Mini-Gymi API docs description",
        contact=openapi.Contact(email="dev@jungledevs.com"),
    ),
    # TODO: Handle login/permission classes
    public=True,  # Check if should be true on your repository
    permission_classes=(permissions.AllowAny,),  # Check if all users should be allowed to see the Swagger
)

###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include('booking.urls')),
    url(r'^', include('payments.urls')),
]

if settings.ENVIRONMENT != 'production':
    urlpatterns += [
        # Swagger URLs
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_v1_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_v1_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_v1_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

