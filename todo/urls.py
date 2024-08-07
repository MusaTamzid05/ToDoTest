from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django.contrib.auth.urls")),
    path("", include("account.urls")),
    path("tasks/", include("tasks.urls")),
    path("api/", include("api.urls")),
]



