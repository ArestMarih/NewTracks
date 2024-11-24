
from django.contrib import admin
from django.urls import path
from trak.views import main, deleters, Poster, edit, getQ,done
from trak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('deleters/<int:id>/', views.deleters),
    path('done/<int:id>/', views.done),
    path('Poster/', views.Poster),
    path('edit/<int:id>/',views.edit),
    path('getQ/<int:pk>/',views.getQ)
   
]
