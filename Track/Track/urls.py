
from django.contrib import admin
from django.urls import path
from trak.views import main, deleters
from trak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('deleters/<int:id>/', views.deleters),
]
