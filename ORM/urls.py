from django.urls import path
from .views import *

urlpatterns = [
    path('1/', index_1),
    path('2/', index_2),
    path('3/', index_3),
]
