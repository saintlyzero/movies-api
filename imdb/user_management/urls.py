from django.urls import path

from .views import UserController 

urlpatterns = [
    path('', UserController.as_view())
]