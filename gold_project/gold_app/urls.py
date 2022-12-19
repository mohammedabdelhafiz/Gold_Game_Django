from django.urls import path     
from . import views
urlpatterns = [
    path('Gold', views.index),
    path('calculate',views.calculate),
    path('reset',views.reset),
    
]
