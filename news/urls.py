from django.urls import path
from .views import home_page, news

urlpatterns = [
    path('', home_page),
    path('news/', news)
]
