from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as url_swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include("accounts.urls")),
    path('api/v1/blog/', include("blog.urls")),
]

urlpatterns += url_swagger
