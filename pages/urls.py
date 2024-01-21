from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view, name='index'), 
    path('demand/', views.second_view, name='demand'), 
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

# Добавьте следующую строку, чтобы обрабатывать статические файлы в режиме разработки
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

