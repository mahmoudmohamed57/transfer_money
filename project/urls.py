from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

admin.site.site_header = "Account Transfer Task Admin"
admin.site.site_title = "Account Transfer Task Admin Portal"
admin.site.index_title = "Welcome to Account Transfer Task Admin Portal"

urlpatterns = [
    path("", lambda request: HttpResponse("Welcome to the Account Transfer Task!")),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)