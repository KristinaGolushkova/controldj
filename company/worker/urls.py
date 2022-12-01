from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='p_delete'),
    path('post/new/', BlogCreateView.as_view(), name='p_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='p_edit'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='p_detail'),
    path('', BlogListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
