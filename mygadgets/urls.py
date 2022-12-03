from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = (
    [
    path('admin/', admin.site.urls),
    path("", include("user.urls", namespace="user")),
  
    # path("tinymce/", include("tinymce.urls")),
    
]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
admin.site.site_header = "ecom Administration"
admin.site.site_title = "ecom Admin Portal"
admin.site.index_title = "Welcome to ecom Admin Portal"