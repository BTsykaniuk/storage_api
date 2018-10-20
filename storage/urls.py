from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


schema_view = get_schema_view(title='Storage API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    path('', schema_view, name="docs"),
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'), namespace='api'))
]
