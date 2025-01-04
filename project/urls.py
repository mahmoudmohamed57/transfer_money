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
