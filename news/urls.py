from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('news/', news),
    path('news1/', news1)
]
