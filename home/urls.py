from home.views import *
from django.urls import path
from .import views
urlpatterns = [
  path('',views.index),
  path('csv/',views.some_view,name="csv"),
  path('xml/',views.my_serialize ,name="xml"),
]