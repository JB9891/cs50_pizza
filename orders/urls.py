from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("order", views.order, name="order")  # TODO add a user ID
]
