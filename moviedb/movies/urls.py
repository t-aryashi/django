from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('add_movie/', views.add_movie, name='add_movie'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
