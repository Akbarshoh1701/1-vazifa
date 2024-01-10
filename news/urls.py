from django.urls import path
from .views import hom_pech, news

urlpatterns = [
    path('', hom_pech),
    path('news/', news)

]
