
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('service/', include('service.urls')),
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
