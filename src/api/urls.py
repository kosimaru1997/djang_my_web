from django.urls import path

from . import views
from .controller import contact_controller

urlpatterns = [
    path("", views.index),
    path("test", contact_controller.index)
]
