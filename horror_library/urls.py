
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from .views import index
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django_nextjs.urls")),
    path("", index, name="index"),
    path('auth/', include('account.urls')),
    path('library/', include('book.urls')),
    # path('auth/', include('rest_framework.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
