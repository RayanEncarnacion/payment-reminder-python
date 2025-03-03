from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("app/", include("payment_reminder.urls")),
    path("admin/", admin.site.urls),
]