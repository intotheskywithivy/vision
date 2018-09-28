from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('/', include('vision.urls')),
    path('admin/', admin.site.urls),
]
