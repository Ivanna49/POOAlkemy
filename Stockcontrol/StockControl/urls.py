from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('compra.urls')),
    path('admin/', admin.site.urls),
    path('compra/', include('compra.urls'))
] 
