from django.contrib import admin
from django.urls import path, include

handler404 = "base.views.handler404"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]