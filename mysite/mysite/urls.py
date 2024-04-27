from django.contrib import admin
from django.urls import include, path
from .views import home
from .views import checkout


urlpatterns = [
    # Include the URL patterns from the 'books' app
    path("admin/", admin.site.urls),  # admin URL pattern
    path("", home, name='home'),
    path("checkout/", checkout, name='checkout')
    
]