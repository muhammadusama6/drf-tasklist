from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasklist/", include('tasklist.urls')),
    path('user/', include('authenticationApi.urls'))
]
