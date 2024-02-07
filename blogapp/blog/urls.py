from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path("", views.index,name="home"),
    path("index/", views.index,name="index"),
    path("blogs/", views.blogs,name="blogs"),
    path('blog/<int:blog_id>/', views.blog_details, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)