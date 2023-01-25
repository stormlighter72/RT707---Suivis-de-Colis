from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ServerWeb/', include('ServerWeb.urls')),
    path('admin/', admin.site.urls),
]

