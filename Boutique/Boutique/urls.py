from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('app_stock.urls')),
    path('personnel/', include('app_personnel.urls')),
    path('auth/', include('app_auth.urls')),
]
