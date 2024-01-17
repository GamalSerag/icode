
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from demo import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/landing/', include('landing.urls')),
    path('api/services/', include('service.urls')),
    path('api/blogs/', include('blog.urls')),
    path('api/about/', include('about.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/home-content/', include('home.urls')),
    path('api/footer/', include('footer.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)