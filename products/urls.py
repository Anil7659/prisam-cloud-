from django.urls import path
from .views  import views
from products.views import *

urlpatterns = [
    path('', views.index),
    path('new', views.new)
    
]


    