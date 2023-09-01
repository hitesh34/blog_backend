from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import LatestPostIdView  # Import your LatestPostIdView here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include your app's URLs here
    # ... other URL patterns
    path('latest-post-id/', LatestPostIdView.as_view(), name='latest-post-id'),  # Remove the slash here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
