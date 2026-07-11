"""
Root URL configuration for the Savory Table project.

Delegates to each app's own urls.py to keep routing modular and clean.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-03289472776/', admin.site.urls),

    # App-level URL includes (each app owns its own namespace)
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('menu/', include('menu.urls', namespace='menu')),
    path('reservations/', include('reservations.urls', namespace='reservations')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
]

# Serve user-uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom admin branding
admin.site.site_header = 'Savory Table Administration'
admin.site.site_title = 'Savory Table Admin Portal'
admin.site.index_title = 'Welcome to the Savory Table Dashboard'