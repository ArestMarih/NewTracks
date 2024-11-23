
from django.contrib import admin
from django.urls import path
from trak.views import main, deleters, Poster, done, edit, getQ
from trak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('deleters/<int:id>/', views.deleters),
    path('Poster/', views.Poster),
    path('done/<int:id>/', views.done),
    path('edit/<int:id>/',views.edit),
    path('getQ/<int:pk>/',views.getQ),
]
