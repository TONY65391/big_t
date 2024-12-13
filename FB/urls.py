from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.create),
    path('create/database/', views.database, name = 'database'),
    #path('create/database/<int:id>', views.database, name = 'database')
]