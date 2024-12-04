
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from trak.views import main, deleters, Poster, done, edit, getQ, test, AddFinance, AddCat
from trak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('deleters/<int:id>/', views.deleters),
    path('done/<int:id>/', views.done),
    path('Poster/', views.Poster),
    path('done/<int:id>/<int:exp>/', views.done),
    path("notdone/<int:id>/<int:exp>/", views.notDone),
    path('edit/<int:id>/',views.edit),
    path('getQ/<int:pk>/',views.getQ),
    path("AddFinance/<int:id>/", views.AddFinance),
    path('AddCat/', views.AddCat),
    path('test/', test) 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)