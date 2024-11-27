
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from trak.views import main, deleters, Poster, done, edit, getQ, test
from trak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('deleters/<int:id>/', views.deleters),
    path('Poster/', views.Poster),
    path('done/<int:id>/', views.done),
    path('edit/<int:id>/',views.edit),
    path('getQ/<int:pk>/',views.getQ),
    path('test/', test)  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)