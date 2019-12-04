from django.urls import path

from .views import MovieController 

urlpatterns = [
    path('', MovieController.as_view()),
]