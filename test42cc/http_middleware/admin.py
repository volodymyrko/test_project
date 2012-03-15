from django.contrib import admin
from http_middleware.models import HttpRequestStore

admin.site.register(HttpRequestStore)
